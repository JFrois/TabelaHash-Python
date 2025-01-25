
<h1>TabelaHash-Python</h1>
    <p>
        Este projeto demonstra a implementação de uma <strong>tabela hash</strong> em Python, com o objetivo de organizar os estados brasileiros em 10 posições de uma tabela, utilizando suas siglas e nomes completos. 
        O projeto inclui funcionalidades adicionais, como a inserção personalizada das iniciais e nome do desenvolvedor na tabela hash.
    </p>

  <h2>Funcionalidades</h2>
    <ol>
        <li><strong>Listagem das Posições da Tabela Hash:</strong> Mostra as 10 posições da tabela hash, mesmo que estejam vazias.</li>
        <li><strong>Inserção Automática de Estados:</strong> Insere automaticamente os estados brasileiros com suas respectivas siglas e nomes completos.</li>
        <li><strong>Inserção Personalizada:</strong> Adiciona as iniciais e o nome completo do desenvolvedor, "JF - Juan Frois", à tabela hash.</li>
        <li><strong>Combinação de Dados:</strong> Exibe uma tabela hash contendo tanto os estados brasileiros quanto o nome personalizado.</li>
        <li><strong>Finalização do Programa:</strong> Permite encerrar o programa de forma segura.</li>
    </ol>

  <h2>Detalhes Técnicos</h2>
    <ul>
        <li>A tabela hash é implementada utilizando <strong>listas encadeadas</strong> para lidar com colisões.</li>
        <li><strong>Regras específicas:</strong>
            <ul>
                <li>A sigla "DF" (Distrito Federal) é sempre armazenada na posição 7 da tabela hash.</li>
                <li>A função hash baseia-se nos valores ASCII das duas primeiras letras da sigla do estado.</li>
            </ul>
        </li>
    </ul>

  <h2>Uso do Programa</h2>
    <ol>
        <li>Clone o repositório:
            <pre><code>git clone https://github.com/seu-usuario/TabelaHash-Python.git</code></pre>
        </li>
        <li>Navegue até o diretório do projeto:
            <pre><code>cd TabelaHash-Python</code></pre>
        </li>
        <li>Execute o programa:
            <pre><code>python tabela_hash.py</code></pre>
        </li>
    </ol>

  <h2>Exemplo de Execução</h2>

  <h3>Menu Interativo</h3>
    <p>O programa apresenta as seguintes opções no menu:</p>
    <ul>
        <li>Listar as posições da tabela hash.</li>
        <li>Listar a tabela hash com os estados e siglas automaticamente adicionados.</li>
        <li>Adicionar "JF - Juan Frois" à tabela hash.</li>
        <li>Combinar os estados e o nome personalizado na tabela hash.</li>
        <li>Finalizar o programa.</li>
    </ul>

  <h3>Demonstrações</h3>
    <h4>1. Listar as Posições da Tabela Hash</h4>
    <p>Exibe todas as posições, indicando se estão preenchidas ou não.</p>
    <img src="https://github.com/user-attachments/assets/893b930e-8c8e-42be-93c2-97a662fa9984" alt="Listar Posições da Tabela Hash">

  <h4>2. Listar Estados na Tabela Hash</h4>
    <p>Adiciona automaticamente os estados e suas siglas.</p>
    <img src="https://github.com/user-attachments/assets/2fa21033-024a-4c98-aec0-2f06e3c69318" alt="Listar Estados na Tabela Hash">

  <h4>3. Adicionar Nome Personalizado</h4>
    <p>Insere "JF - Juan Frois" na tabela.</p>
    <img src="https://github.com/user-attachments/assets/d8e1766f-9b32-4dff-abbd-b7f458975c81" alt="Adicionar Nome à Tabela Hash">

  <h4>4. Combinar Estados e Nome Personalizado</h4>
    <p>Lista todos os estados e o nome adicionado.</p>
    <img src="https://github.com/user-attachments/assets/af9a21ba-9392-4aa2-8920-213dbaaa79aa" alt="Combinar Dados na Tabela Hash">

  <h4>5. Finalizar o Programa</h4>
    <p>Encerramento seguro do programa.</p>
    <img src="https://github.com/user-attachments/assets/6a0fe5a4-0de7-4382-88ba-f08f2661e55e" alt="Finalizar o Programa">

  <h2>Estrutura do Código</h2>

  <h3>Classes</h3>
    <ul>
        <li><strong>ElementoListaEncadeada:</strong> Representa um elemento de uma lista encadeada, contendo a sigla e o nome do estado.</li>
        <li><strong>ListaEncadeada:</strong> Implementa uma lista encadeada para armazenar múltiplos elementos.</li>
        <li><strong>TabelaHash:</strong> Implementa a tabela hash com uma função hash personalizada para organizar os estados.</li>
    </ul>

  <h3>Funções</h3>
    <ul>
        <li><code>hashfuncao(k)</code>: Calcula a posição na tabela hash com base na sigla do estado.</li>
        <li><code>inserirEstados(tabela)</code>: Insere todos os estados na tabela hash.</li>
        <li><code>menu()</code>: Exibe o menu interativo e processa as opções escolhidas pelo usuário.</li>
    </ul>

