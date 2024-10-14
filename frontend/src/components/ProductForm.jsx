import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { createProduto, fetchCategorias } from "../services/api";
import { TextField, Button, Paper, MenuItem, Select, InputLabel, FormControl, Box, Typography } from "@mui/material";

const ProductForm = () => {
  const [nome, setNome] = useState("");
  const [descricao, setDescricao] = useState("");
  const [cor, setCor] = useState("");
  const [preco, setPreco] = useState("");
  const [categoriaId, setCategoriaId] = useState("");
  const [categorias, setCategorias] = useState([]);

  useEffect(() => {
    fetchCategorias()
      .then((response) => {
        setCategorias(response.data.categorias);
      })
      .catch((error) => {
        console.error("Erro ao carregar categorias:", error);
      });
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!nome || !descricao || !preco || !categoriaId) {
      alert("Todos os campos são obrigatórios!");
      return;
    }

    createProduto({ nome, descricao, cor, preco, categoria_id: categoriaId })
      .then(() => {
        alert("Produto criado com sucesso!");
        setNome("");
        setDescricao("");
        setCor("");
        setPreco("");
        setCategoriaId("");
      })
      .catch((error) => {
        console.error("Erro ao criar o produto:", error);
        alert("Erro ao criar o produto.");
      });
  };

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h4" gutterBottom>
        Adicionar Produto
      </Typography>
      <Link to="/" style={{ textDecoration: 'none' }}>
      <Button variant="contained" color="primary" sx={{ marginBottom: 2 }}>
        Lista de produtos
      </Button>
    </Link>
      <Paper sx={{ padding: 2, marginBottom: 3 }}>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            fullWidth
            margin="normal"
            required
          />
          <TextField
            label="Descrição"
            value={descricao}
            onChange={(e) => setDescricao(e.target.value)}
            fullWidth
            margin="normal"
            required
          />
          <TextField
            label="Cor"
            value={cor}
            onChange={(e) => setCor(e.target.value)}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Preço"
            type="number"
            value={preco}
            onChange={(e) => setPreco(e.target.value)}
            fullWidth
            margin="normal"
            required
          />
          <FormControl fullWidth margin="normal">
            <InputLabel id="categoria-label">Categoria</InputLabel>
            <Select
              labelId="categoria-label"
              value={categoriaId}
              onChange={(e) => setCategoriaId(e.target.value)}
              required
            >
              {categorias.map((categoria) => (
                <MenuItem key={categoria.id} value={categoria.id}>
                  {categoria.nome}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
          <Button variant="contained" color="primary" type="submit">
            Adicionar Produto
          </Button>
        </form>
      </Paper>
    </Box>
  );
};

export default ProductForm;
