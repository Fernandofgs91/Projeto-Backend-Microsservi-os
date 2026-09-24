import os
import subprocess
from pathlib import Path

# Diretório onde o script está localizado
BASE_DIR = Path(__file__).resolve().parent

# Conteúdo do Dockerfile para o api_gateway
DOCKERFILE_GATEWAY = """# Etapa de compilação
FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# Etapa de execução
FROM eclipse-temurin:17-jre-jammy
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
"""

# Conteúdo do docker-compose.yml para orquestrar os 3 serviços
DOCKER_COMPOSE_YML = """version: '3.8'

services:
  restricao-service:
    build:
      context: ./restricao-service
      dockerfile: Dockerfile
    container_name: restricao-service
    ports:
      - "8082:8082"
    networks:
      - backend-network

  cliente-service:
    build:
      context: ./cliente_service
      dockerfile: Dockerfile
    container_name: cliente-service
    ports:
      - "8081:8081"
    environment:
      - RESTRICAO_SERVICE_URL=http://restricao-service:8082
    depends_on:
      - restricao-service
    networks:
      - backend-network

  api-gateway:
    build:
      context: ./api_gateway
      dockerfile: Dockerfile
    container_name: api-gateway
    ports:
      - "8080:8080"
    environment:
      - CLIENTE_SERVICE_URL=http://cliente-service:8081
      - RESTRICAO_SERVICE_URL=http://restricao-service:8082
    depends_on:
      - cliente-service
      - restricao-service
    networks:
      - backend-network

networks:
  backend-network:
    driver: bridge
"""

def main():
    print("=== Configurando ambiente Docker para os microsserviços ===")

    # 1. Criar Dockerfile para o api_gateway se não existir
    gateway_dockerfile = BASE_DIR / "api_gateway" / "Dockerfile"
    if not gateway_dockerfile.exists():
        print("-> Criando Dockerfile em: api_gateway/Dockerfile")
        gateway_dockerfile.write_text(DOCKERFILE_GATEWAY, encoding="utf-8")
    else:
        print("-> Dockerfile em api_gateway já existe. Mantendo o existente.")

    # 2. Criar docker-compose.yml na raiz do projeto
    compose_file = BASE_DIR / "docker-compose.yml"
    print("-> Criando/atualizando docker-compose.yml na raiz...")
    compose_file.write_text(DOCKER_COMPOSE_YML, encoding="utf-8")

    # 3. Rodar o docker compose up --build
    print("\n=== Iniciando os contêineres via Docker Compose ===")
    try:
        subprocess.run(["docker", "compose", "up", "--build"], cwd=BASE_DIR, check=True)
    except FileNotFoundError:
        print("\n[ERRO] O comando 'docker' não foi encontrado.")
        print("Certifique-se de que o Docker Desktop está instalado e aberto no seu Windows.")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERRO] Falha ao executar o docker compose (código {e.returncode}).")

if __name__ == "__main__":
    main()