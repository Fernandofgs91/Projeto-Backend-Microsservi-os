package br.edu.iftm.restricao_service.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.edu.iftm.restricao_service.domain.Restricao;
import jakarta.websocket.server.PathParam;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
@RequestMapping("/restricao")
public class RestricaoController {

    @GetMapping("/{cpf}")
    public ResponseEntity<Restricao> getRestricao(@PathVariable String cpf) {
        String cpfBanco = "000.000.000-00";
        Restricao restricao = new Restricao(cpf, false);
        if (cpf.equals(cpfBanco)) {
            restricao.setNomeSujo(true);
        }
        return ResponseEntity.ok().body(restricao);
    }

}
