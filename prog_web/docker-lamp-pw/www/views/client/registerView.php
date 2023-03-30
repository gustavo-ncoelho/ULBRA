<h1>Cadastro do Cliente</h1>

<table class="table table-striped">
    <tr>
        <th>Nome</th>
        <td>
            <?=arrayClient['name']?>
        </td>
    </tr>
    <tr>
        <th>Email</th>
        <td>
            <?=arrayClient['email']?>
        </td>
    </tr>
</table>


<?php
    var_dump($arrayClient);
?>