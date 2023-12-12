package br.com.poo.ap2.services;

import br.com.poo.ap2.model.ClienteModel;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
@Service
public class ClienteServiceImpl implements ClienteService{
    private final ArrayList<ClienteModel> listaClientes = new ArrayList<ClienteModel>();
    private int lastId = 0;

    @Override
    public ArrayList<ClienteModel> findAll() {
        return listaClientes;
    }

    @Override
    public ClienteModel findById(int id) {
        for (int i = 0; i < listaClientes.size(); i++){
            if (listaClientes.get(i).getId() == id){
                return listaClientes.get(i);
            }
        }
        return null;
    }

    @Override
    public ArrayList<ClienteModel> findAllByIdade(int idade) {
        ArrayList<ClienteModel> clientesIdade = new ArrayList<ClienteModel>();
        for (int i = 0; i < listaClientes.size(); i++){
            if (listaClientes.get(i).getIdade() == idade){
                clientesIdade.add(listaClientes.get(i));
            }
        }
        return clientesIdade;
    }

    @Override
    public String save(ClienteModel cliente) {
        lastId += 1;
        cliente.setId(lastId);
        listaClientes.add(cliente);
        return "Cliente cadastrado com sucesso!!!";
    }

    @Override
    public String update(int id, ClienteModel cliente) {
        listaClientes.stream()
                .filter(clienteAtual -> clienteAtual.getId() == id)
                .findFirst()
                .ifPresent(clienteAtual -> {
                    clienteAtual.setNome(cliente.getNome());
                    clienteAtual.setIdade(cliente.getIdade());
                    clienteAtual.setProfissao(cliente.getProfissao());
                });
        return "Cliente atualizado com sucesso!!!";
    }

    @Override
    public String delete(int id) {
        listaClientes.removeIf(cliente -> cliente.getId() == id);
        return "Cliente deletado com sucesso!!!";
    }
}
