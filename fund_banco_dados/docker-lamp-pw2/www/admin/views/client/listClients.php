<h1>Listagem de Clientes</h1>
<table class="table table-stripped">
    <tr>
        <th>ID Cliente</th>
        <th>Nome</th>
        <th>Email</th>
        <th>Telefone</th>
        <th>Endereço</th>
        <th>Ações</th>
    </tr>

    <?php
        foreach ($arrayClients as $client) {
    ?>

        <tr>
            <td>
                <?=$client['idClient']?>
            </td>
            <td>
                <?=$client['name']?>
            </td>
            <td>
                <?=$client['email']?>
            </td>
            <td>
                <?=$client['phone']?>
            </td>
            <td>
                <?=$client['address']?>
            </td>
            <td>
                <?php
                    if(is_file("assets/img/client/{$client['idClient']}.jpg")){
                        echo "<img class='img-fluid' src='assets/img/client/{$client['idClient']}.jpg'>";
                    }else{
                        echo 'não tem foto';
                    }
                ?>
            </td>
            <td>
                <a class="btn btn-primary bi bi-eye" href="?controller=client&action=detailsClient&id=<?=$client['idClient']?>">
                   
                </a>
            </td>
            <td>
                <a class="btn btn-warning bi bi-pencil-square" href="?controller=client&action=updateClient&id=<?=$client['idClient']?>">
                   
                </a>
            </td>
            <td>
                <a class="btn btn-danger bi bi-x-lg" href="?controller=client&action=deleteClient&id=<?=$client['idClient']?>">
                </a>
            </td>
        </tr>

    <?php
        }
    ?>

</table>