package br.com.poo.ap2.services;

import br.com.poo.ap2.model.ClienteModel;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
@Service
public interface ClienteService {
    ArrayList<ClienteModel> findAll();
    ClienteModel findById(int id);
    ArrayList<ClienteModel> findAllByIdade(int idade);
    String save(ClienteModel cliente);
    String update(int id, ClienteModel cliente);
    String delete(int id);
}
