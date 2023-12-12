package as.demo.DTOs;

import as.demo.Entities.Client;
import lombok.AllArgsConstructor;
import lombok.Data;
import java.util.ArrayList;
import java.util.List;

@Data
@AllArgsConstructor
public class ClientDTO {
    private String name;
    private int age;
    private String job;

    public static ClientDTO convertToDTO(Client client){
        return new ClientDTO(client.getName(), client.getAge(), client.getJob());
    }

    public static Client convertToClient(ClientDTO clientDTO){
        return new Client(clientDTO.getName(), clientDTO.getAge(), clientDTO.getJob());
    }

    public static List<ClientDTO> convertToDTO(List<Client> clientList){
        List<ClientDTO> clientDTOList = new ArrayList<ClientDTO>();
        for (int i = 0; i < clientList.size(); i++){
            clientDTOList.add(new ClientDTO(clientList.get(i).getName(), clientList.get(i).getAge(), clientList.get(i).getJob()));
        }
        return clientDTOList;
    }
}
