package br.edu.iftm.restricao_service.domain;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Restricao {

    private String cpf;

    private Boolean nomeSujo;

}
