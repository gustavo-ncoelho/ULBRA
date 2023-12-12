package as.demo.Controllers;

import as.demo.DTOs.ClientDTO;
import as.demo.Services.ClientService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/clients")
public class ClientController {
    ClientService clientService;
    @Autowired
    public ClientController(ClientService clientService){
        this.clientService = clientService;
    }

    @GetMapping
    public List<ClientDTO> getClients(){
        return clientService.getClients();
    }
    @PostMapping
    public void saveClient(@RequestBody ClientDTO clientDTO){
        clientService.saveClient(clientDTO);
    }
    @PutMapping("/{id}")
    public void updateClient(@PathVariable Integer id,@RequestBody ClientDTO clientDTO){
        clientService.updateClient(id, clientDTO);
    }
    @DeleteMapping("/{id}")
    public void deleteClient(@PathVariable Integer id){
        clientService.deleteClient(id);
    }
}
