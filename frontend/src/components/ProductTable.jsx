import React, { useEffect, useState, useCallback } from 'react';
import { Link } from 'react-router-dom';
import {
  Box,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  CircularProgress,
  TextField,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  Typography,
  Pagination,
  IconButton,
  Button
} from '@mui/material';
import { fetchProdutos, deleteProduto, fetchCategorias } from '../services/api'; 
import DeleteIcon from '@mui/icons-material/Delete';

const ProductTable = () => {
  const [produtos, setProdutos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [totalPages, setTotalPages] = useState(1); 
  const [currentPage, setCurrentPage] = useState(1); 
  const [categorias, setCategorias] = useState([]);
  const [filters, setFilters] = useState({
    limit: 10,
    offset: 0,
    order_by: 'id',
    order_direction: 'asc',
    nome: '',
    categoria_id: '',
  });

  const getProdutos = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);

      const queryParams = { ...filters, offset: (currentPage - 1) * filters.limit };

      if (!queryParams.nome) {
        delete queryParams.nome;
      }
      if (!queryParams.categoria_id) {
        delete queryParams.categoria_id;
      }

      const response = await fetchProdutos(queryParams);
      setProdutos(response.data.produtos);
      setTotalPages(Math.ceil(response.data.total / filters.limit)); 
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }, [filters, currentPage]); 

  const getCategorias = useCallback(async () => {
    try {
      const response = await fetchCategorias(); 
      setCategorias(response.data.categorias);
    } catch (err) {
      setError(err);
    }
  }, []);

  useEffect(() => {
    getProdutos();
    getCategorias();
  }, [getProdutos, getCategorias]); 

  const handleFilterChange = (e) => {
    setFilters({
      ...filters,
      [e.target.name]: e.target.value,
    });
  };

  const handlePageChange = (event, page) => {
    setCurrentPage(page); 
  };

  const handleDelete = async (id) => {
    try {
      await deleteProduto(id);
      getProdutos(); 
    } catch (err) {
      setError(err);
    }
  };

  const categoriasMap = categorias.reduce((acc, categoria) => {
    acc[categoria.id] = categoria.nome; 
    return acc;
  }, {});
  

  if (loading) return (
    <div className='flex justify-center items-center w-screen h-screen'>
      <CircularProgress />
    </div>)

  if (error) return <Typography color="error">Error: {error.message}</Typography>;

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h4" gutterBottom>
        Lista de Produtos
      </Typography>
      <Link to="/novo" style={{ textDecoration: 'none' }}>
      <Button variant="contained" color="primary" sx={{ marginBottom: 2 }}>
        Adicionar Produto
      </Button>
    </Link>
      <Box
        component={Paper}
        sx={{ padding: 2, marginBottom: 3, display: 'flex', gap: 2, flexWrap: 'wrap' }}
      >
        <TextField
          label="Nome"
          name="nome"
          value={filters.nome}
          onChange={handleFilterChange}
          variant="outlined"
          size="small"
          placeholder="Pesquisar por nome"
        />
          <Select
            name="categoria_id"
            value={filters.categoria_id}
            onChange={handleFilterChange}
            displayEmpty
            size='small'
          >
            <MenuItem value="">
              <em>Selecionar categoria</em>
            </MenuItem>
            {categorias.map((categoria) => (
              <MenuItem key={categoria.id} value={categoria.id}>
                {categoria.nome}
              </MenuItem>
            ))}
          </Select>
        <FormControl variant="outlined" size="small">
          <InputLabel>Ordenar por</InputLabel>
          <Select
            label="Ordenar por"
            name="order_by"
            size='small'
            value={filters.order_by}
            onChange={handleFilterChange}
            displayEmpty
          >
            <MenuItem value="id">ID</MenuItem>
            <MenuItem value="nome">Nome</MenuItem>
            <MenuItem value="preco">Preço</MenuItem>
          </Select>
        </FormControl>
        <FormControl variant="outlined" size="small">
          <InputLabel>Direção</InputLabel>
          <Select
            label="Direção"
            name="order_direction"
            value={filters.order_direction}
            onChange={handleFilterChange}
          >
            <MenuItem value="asc">Ascendente</MenuItem>
            <MenuItem value="desc">Descendente</MenuItem>
          </Select>
        </FormControl>
      </Box>

      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Nome</TableCell>
              <TableCell>Descrição</TableCell>
              <TableCell>Cor</TableCell>
              <TableCell>Categoria</TableCell>
              <TableCell>Preço</TableCell>
              <TableCell>Preço Promocional</TableCell>
              <TableCell>Ações</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {produtos.map((produto) => (
              <TableRow key={produto.id}>
                <TableCell>{produto.nome}</TableCell>
                <TableCell>{produto.descricao}</TableCell>
                <TableCell>{produto.cor}</TableCell>
                <TableCell>{categoriasMap[produto.categoria_id] || 'Categoria Desconhecida'}</TableCell>
                <TableCell>{produto.preco}</TableCell>
                <TableCell>{produto.preco_com_desconto}</TableCell>
                <TableCell>
                  <IconButton
                    color="error"
                    onClick={() => handleDelete(produto.id)}
                  >
                    <DeleteIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Pagination
        count={totalPages}
        page={currentPage}
        onChange={handlePageChange}
        sx={{ marginTop: 2 }}
      />
    </Box>
  );
};

export default ProductTable;
