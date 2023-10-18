import React, { useState, useEffect } from "react";
import axios from "axios";

const ListaDeItens = () => {
  const [itens, setItens] = useState([]);

  useEffect(() => {
    // Função assíncrona para fazer a requisição GET usando Axios
    const fetchData = async () => {
      try {
        // Fazendo a requisição GET para a API
        const response = await axios.get("http://127.0.0.1:8000/items/");
        console.log("response.data");
        console.log(response.data);

        // Atualizando o estado com os dados da resposta
        setItens(response.data);
      } catch (error) {
        // Lidando com erros, você pode exibir uma mensagem de erro ou fazer o que for necessário
        console.error("Erro ao buscar itens:", error);
      }
    };

    // Chamando a função assíncrona para fazer a requisição quando o componente monta
    fetchData();
  }, []); // O segundo argumento vazio faz com que o useEffect seja executado apenas uma vez, equivalente a componentDidMount

  return (
    <div>
        {itens.map((item) => (
          <div key={item.id}>
            <p>{item.name}</p>
            <p>{item.description}</p>
            <p>{item.power_category}</p>
            <p>{item.rarity}</p>
            <p>{item.type}</p>
          </div>
        ))}
    </div>
  );
};

export default ListaDeItens;
