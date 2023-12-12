package br.com.meuprojeto.webservice;
import java.util.ArrayList;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
@RequestMapping("/")
public class WebserviceApplication {
	ArrayList<Cliente> listaClientes = new ArrayList<Cliente>();

	ArrayList<Cliente> getListaClientes(){
		return listaClientes;
	}

	@PostMapping()
	public void incluirCliente(@RequestBody Cliente cliente){
		listaClientes.add(cliente);
	}

	@GetMapping()
	public ArrayList<Cliente> listarClientes(){
		return getListaClientes();
	}

	@GetMapping("/{nome}")
	public Cliente getClientePeloNome(@PathVariable String nome){
		for (int i = 0; i < listaClientes.size(); i++){
			if (listaClientes.get(i).getNome().contains(nome)){
				return listaClientes.get(i);
			}
		}
		return null;
	}

	public static void main(String[] args) {
		SpringApplication.run(WebserviceApplication.class, args);
	}

}
