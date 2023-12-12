<h1>Dados do cadastro</h1>

<table class="table table-stripped">
    <tr>
        <th>Nome</th>
        <td>
            <?=$arrayClient["name"]?>
        </td>
    </tr>
    <tr>
        <th>Telefone</th>
        <td>
            <?=$arrayClient["phone"]?>
        </td>
    </tr>
    <tr>
        <th>Email</th>
        <td>
            <?=$arrayClient["email"]?>
        </td>
    </tr>
    <tr>
        <th>Senha</th>
        <td>
            <?=$arrayClient["password"]?>
        </td>
    </tr>
    <tr>
        <th>Sexo</th>
        <td>
            <?=$arrayClient["gender"]?>
        </td>
    </tr>
    <tr>
        <th>Stack</th>
        <td>
            <?php
                if (empty($arrayClient['stack'])) {
                    echo 'Você não selecionou nenhuma stack';
                }
                else {
                    foreach ($arrayClient['stack'] as $stack) {
                        echo "$stack ";
                    }
                }
            ?>
        </td>
    </tr>
    <tr>
        <th>Trabalhando?</th>
        <td>
            <?=$arrayClient["trabalhando"]?>
        </td>
    </tr>
    <tr>
        <th>Faixa de Idade</th>
        <td>
            <?=$arrayClient["faixaIdade"]?>
        </td>
    </tr>
    <tr>
        <th>Objetivo para o futuro</th>
        <td>
            <?=$arrayClient["objetivo"]?>
        </td>
    </tr>
</table>