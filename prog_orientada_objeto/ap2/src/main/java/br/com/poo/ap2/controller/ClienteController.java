package br.com.poo.ap2.controller;

import java.util.ArrayList;

import br.com.poo.ap2.model.ClienteModel;
import br.com.poo.ap2.services.ClienteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/clientes")
public class ClienteController {

    private final ClienteService service;

    @Autowired
    public ClienteController(ClienteService service) {
        this.service = service;
    }

    @GetMapping()
    public ResponseEntity<ArrayList<ClienteModel>> getClientes() {
        return new ResponseEntity<>(service.findAll(), HttpStatus.OK);
    }

    @GetMapping("/{id}")
    public ResponseEntity<ClienteModel> getClienteById(@PathVariable int id){
        return new ResponseEntity<>(service.findById(id), HttpStatus.NOT_FOUND);
    }

    @GetMapping("/por-idade")
    public ResponseEntity<ArrayList<ClienteModel>> getClientesByIdade(@RequestParam int idade){
        return new ResponseEntity<>(service.findAllByIdade(idade), HttpStatus.OK);
    }

    @PostMapping
    public ResponseEntity<String> saveCliente(@RequestBody ClienteModel cliente) {
        return new ResponseEntity<>(service.save(cliente) , HttpStatus.CREATED);
    }

    @PutMapping("/{id}")
    public ResponseEntity<String> updateCliente(@PathVariable int id, @RequestBody ClienteModel cliente) {
        return new ResponseEntity<>(service.update(id,cliente), HttpStatus.OK);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteCliente(@PathVariable int id) {
        return new ResponseEntity<>(service.delete(id), HttpStatus.OK);
    }
}
