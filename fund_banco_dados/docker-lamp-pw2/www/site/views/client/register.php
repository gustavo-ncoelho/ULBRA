<div class="card p-5 m-5 w-10">
    <form action="?controller=client&action=registerView" method="POST">
        <div class="mb-3">
            <label for="nome" class="form-label">Nome:</label>
            <input type="text" class="form-control" id="name" name="name" required>
        </div>
        <div class="mb-3">
            <label for="telefone" class="form-label">Telefone:</label>
            <input type="text" class="form-control" id="phone" name="phone" required>
        </div>
        <div class="mb-3">
            <label for="email" class="form-label">Email:</label>
            <input type="text" class="form-control" id="email" name="email" required>
        </div>
        <div class="mb-3">
            <label for="email" class="form-label">Senha:</label>
            <input type="password" class="form-control" id="password" name="password" required>
        </div>


        <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="gender" id="radioMasculino" value="Masculino" checked>
            <label class="form-check-label" for="inlineRadio1">Masculino</label>
        </div>
        <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="gender" id="radioFeminino" value="Feminino">
            <label class="form-check-label" for="inlineRadio2">Feminino</label>
        </div>

        <div class="mt-3">
            <label class="form-check-label">Qual sua stack?</label>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="Frontend" name="front" id="front">
                <label class="form-check-label" for="defaultCheck1">
                    Frontend
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="Backend" name="back" id="back">
                <label class="form-check-label" for="defaultCheck1">
                    Backend
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="Devops" name="devops" id="devops">
                <label class="form-check-label" for="defaultCheck1">
                    Devops
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="Data" name="data" id="data">
                <label class="form-check-label" for="defaultCheck1">
                    Dados
                </label>
            </div>

            <div>
                <label class="form-check-label mt-3">Já está trabalhando fixo?</label>
                <select class="form-select" aria-label="trabalhando" name="working" required>
                    <option value="Sim">Sim</option>
                    <option value="Não">Não</option>
                    <option value="Sou Freelancer">Sou Freelancer</option>
                </select>
            </div>

            <div>
                <label class="form-check-label mt-3">Qual sua faixa de idade?</label>
                <select class="form-select" multiple aria-label="faixaIdade" name="age" required>
                    <option value="Menos de 18">Menos de 18</option>
                    <option value="18 a 30 anos">18 a 30 anos</option>
                    <option value="31 a 50 anos">31 a 50 anos</option>
                    <option value="51+ anos">51+ anos</option>
                </select>
            </div>

            <div class="input-group mt-3">
                <span class="input-group-text">Objetivo para o futuro:</span>
                <textarea class="form-control" aria-label="textarea" name="objective" required></textarea>
            </div>


            <div>
                <button type="submit" class="btn btn-primary mt-3">Enviar</button>
            </div>
        </div>
    </form>
</div>