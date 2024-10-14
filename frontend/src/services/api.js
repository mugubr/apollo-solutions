import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const fetchProdutos = (params) => api.get("/produtos", { params });
export const fetchProdutoById = (id) => api.get(`/produtos/${id}`);
export const createProduto = (produto) => api.post("/produtos", produto);
export const updateProduto = (id, produto) =>
  api.put(`/produtos/${id}`, produto);
export const deleteProduto = (id) => api.delete(`/produtos/${id}`);
export const fetchCategorias = () => api.get("/categorias/");