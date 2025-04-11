Estrutura do Relatório:

1 - Introdução
2 - Função de Cada Integrante
3 - Funcionalidades do Projeto
4 - Desafios Encontrados e Como Foram Resolvidos
5 - Conclusão

1. Introdução

Este projeto consiste em uma API desenvolvida com Flask para gerenciar Alunos, Professores e Turmas, permitindo a realização de operações de CRUD (criar, ler, atualizar e excluir) e retornando os dados no formato JSON. O objetivo foi criar uma solução simples, funcional e que facilitasse o gerenciamento de informações escolares.

A API foi testada utilizando o Postman e o código foi versionado no GitHub, o que possibilitou um controle das alterações e, uma colaboração organizada entre os membros da equipe.

2. Função de Cada Integrante

Jonatha e Caique: Responsáveis pelo desenvolvimento do código base, configuração do Flask e integração com o banco de dados.

Rafael e Letícia: Responsáveis pelos testes da API, garantindo que a aplicação lidasse corretamente com erros e entradas inválidas através do uso do try/catch.

Otávio: Foi responsável pela documentação do projeto, detalhando o funcionamento da API, e contribuiu no desenvolvimento do código.

3. Funcionalidades do Projeto

A API desenvolvida tem como objetivo centralizar e facilitar o gerenciamento de informações essenciais dentro de uma escola, como os dados de alunos, professores e turmas. Com ela, é possível realizar operações de CRUD (criar, ler, atualizar e excluir) de forma muito mais simples e organizada.

Para os alunos, a API permite cadastrar novos alunos com informações como nome, idade, email e notas, que são armazenadas de forma estruturada, facilitando a consulta e análise detalhada. Também é possível atualizar esses dados caso haja mudanças, como a alteração de nota ou correção de informações pessoais. Além disso, o sistema possibilita a exclusão de registros de alunos, caso necessário, mantendo o banco de dados sempre atualizado, e sem problemas aparente.

Em relação aos professores, a API permite a criação de novos cadastros, onde são registrados dados como nome, disciplina e email. Assim como para os alunos, é possível alterar as informações de um professor. Isso garante que o gerenciamento dos professores seja eficiente e, sempre reflita a realidade da instituição.

Para as turmas, a API oferece a funcionalidade de cadastrar novas turmas, associando um professor responsável e um ano letivo. Esse cadastro também pode ser atualizado, caso a turma mude de nome ou o ano letivo seja alterado, e turmas desnecessárias podem ser excluídas.

Além disso, a API permite associar alunos a turmas, ou seja, quando um aluno é matriculado em uma turma, essa associação fica registrada, e a qualquer momento podemos consultar quais alunos pertencem a qual turma. Caso um aluno precise ser transferido para outra turma, essa alteração pode ser feita facilmente.

A API, no geral, oferece uma forma prática e muito eficiente de gerenciar a vida acadêmica dos alunos, os dados dos professores e a organização das turmas. A estrutura foi construída de modo que todos esses processos sejam realizados de forma relativamente simples, com a possibilidade de integrar facilmente com outras plataformas, já que todas as respostas são enviadas em formato JSON.

4. Desafios Encontrados e Como Foram Resolvidos

Um dos desafios foi a execução ao fazer os testes, especialmente com try/catch para lidar com erros. No começo, foi um pouco trabalhoso, mas, com o tempo, o processo funcionou com êxito ao realizar os testes necessários para garantir que a API funcionasse direitinho.

5. Conclusão

O projeto foi concluído com sucesso, com a API funcionando conforme os requisitos propostos. Todas as operações de CRUD para alunos, professores e turmas foram implementadas corretamente. Apesar dos desafios encontrados, a equipe conseguiu superar as dificuldades e entregar uma solução funcional, bem documentada e testada.
