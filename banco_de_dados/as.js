const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 3000;


const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'asbd'
});

connection.connect((err) => {
  if (err) {
    console.error('Erro ao conectar ao banco de dados:', err);
    throw err;
  }
  console.log('Conectado ao banco de dados MySQL');
});

app.use(cors());
app.use(bodyParser.json());

// ----- GET ------
app.get('/api/atletas', (req, res) => {
  connection.query('SELECT * FROM atletas', (err, results) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json(results);
  });
});

// ----- POST ------
app.post('/api/atletas', (req, res) => {
  const { nome, idade, esporte, equipe } = req.body;
  connection.query('INSERT INTO atletas (nome, idade, esporte, equipe) VALUES (?, ?, ?, ?)',
    [nome, idade, esporte, equipe],
    (err, results) => {
      if (err) {
        res.status(500).json({ error: err.message });
        return;
      }
      res.json({ message: 'Atleta criado com sucesso', id: results.insertId });
    });
});

// ----- DELETE ------
app.delete('/api/atletas/:id', (req, res) => {
  const { id } = req.params;
  connection.query('DELETE FROM atletas WHERE id = ?', id, (err, results) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    res.json({ message: 'Atleta removido com sucesso' });
  });
});


app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});