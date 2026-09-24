package br.edu.iftm.cliente_service.cliente_service.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.edu.iftm.cliente_service.cliente_service.client.ClienteClient;
import br.edu.iftm.cliente_service.cliente_service.domain.Cliente;
import lombok.AllArgsConstructor;

@RestController
@RequestMapping("/cliente")
@AllArgsConstructor
public class ClienteController {

    private ClienteClient clienteClient;

    @GetMapping("/{cpf}")
    public ResponseEntity<Cliente> getCpf(@PathVariable String cpf) {
        Cliente cliente = new Cliente();
        cliente.setCpf(cpf);
        cliente.setNome("Fernandinho");
        cliente.setRestricao(clienteClient.isCpfValido(cpf));
        return ResponseEntity.ok().body(cliente);
    }

}
