package br.edu.iftm.cliente_service.cliente_service.client;

import org.springframework.stereotype.Component;
import org.springframework.web.client.RestClient;

import tools.jackson.databind.JsonNode;

@Component
public class ClienteClient {

    private final RestClient restClient;

    public ClienteClient(RestClient.Builder builder) {
        this.restClient = builder
                .baseUrl("http://localhost:8080/restricao")
                .build();
    }

    public boolean isCpfValido(String cpf) {
        JsonNode resposta = restClient.get()
                .uri("/{cpf}", cpf)
                .retrieve()
                .body(JsonNode.class);

        return resposta != null
                && resposta.path("nomeSujo").asBoolean(false);
    }

}
