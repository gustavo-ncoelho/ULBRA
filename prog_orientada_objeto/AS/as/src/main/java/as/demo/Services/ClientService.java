package as.demo.Services;

import as.demo.DTOs.ClientDTO;
import as.demo.Entities.Client;
import as.demo.Exceptions.ClientNotFoundException;
import as.demo.Repositories.ClientRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.List;
import java.util.Optional;

@Service
public class ClientService {
    public ClientRepository clientRepository;
    @Autowired
    public ClientService(ClientRepository clientRepository){
        this.clientRepository = clientRepository;
    }

    public List<ClientDTO> getClients(){
       return ClientDTO.convertToDTO(clientRepository.findAll());
    }

    public void saveClient(@RequestBody ClientDTO clientDTO){
        Client client = ClientDTO.convertToClient(clientDTO);
        Client savedClient = clientRepository.save(client);
    }

    public ClientDTO updateClient(Integer id, ClientDTO clientDTO) {
        Optional<Client> optionalClient = clientRepository.findById(id);
        if (optionalClient.isPresent()) {
            Client clientToUpdate = optionalClient.get();
            clientToUpdate.setName(clientDTO.getName());
            clientToUpdate.setAge(clientDTO.getAge());
            clientToUpdate.setJob(clientDTO.getJob());

            Client updatedClient = clientRepository.save(clientToUpdate);
            return ClientDTO.convertToDTO(updatedClient);
        } else{
            throw new ClientNotFoundException("Cliente não encontrado");
        }
    }

    public void deleteClient(Integer id){
        clientRepository.deleteById(id);
    }
}








