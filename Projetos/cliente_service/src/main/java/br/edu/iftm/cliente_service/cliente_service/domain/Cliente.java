package br.edu.iftm.cliente_service.cliente_service.domain;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Cliente {

    private String cpf;

    private String nome;

    private Boolean restricao;

}
