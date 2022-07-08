'''
How to fix remote: Permission to (repo.git) denied

git push or git push -u origin master = error 403

> logar na conta github, 
> Entrar no gerenciador de credenciais do windows
> remova a credencial git https://github.com
> volte ao terminal e conecte novamente com a conta github usando o comando: git push -u origin master
> abrirá um pop up para poder logar na conta github


===================================================================================================================================
1ª Etapa - Git.

1. Criar pasta em algum lugar do computador onde será a área de trabalho. 

2. criar uma pasta de repositório. 

3. abra o git bash dentro da pasta.

4. verifique se a versão do bash está atualizada: git version

5. dentro da pasta, use o git para abrir o vs code: code . 

6. Crie um README.md - md = marked down, linguagem de marcação. 

7. Escreva algo dentro do documento e salve. 

8. Apartir daqui pode usar tanto o git bash quanto o terminal vscode

9. O primeiro passo agora é iniciar o Git: git init

10. Será gerado um arquivo git dentro da pasta que não deve ser apagado por nada. E desta vez a pasta é transformada em branch MASTER.

11. no terminal/git bash adicione um arquivo para espera de commit com o comando: git add README.md  *pode ser qualquer arquivo que queira adicionar ao commit

12 Para saber a situação atual: git status

13. para commitar o arquivo: git commit -m "mensagem do commit"

14. git status novamente, para saber se tudo funcionou corretamente. 

15. Para mudar a nomenclatura, caso a empresa que esteja trabalhando use main e não master, basta trocar a nomenclatura com: git branch -M "main"


2ª etapa - GitHub.

1. Entre no Github. 

2. Entrar em repositórios > new

3. Crie um nome para o repositório, pode ser o mesmo existente na pasta, ou pode criar outro. (Se criar outro uma nova pasta é criada)

4. Escolha se será público ou privado.

5. add a Readme file, se não tiver criado manualmente, caso tenha criado um antes, não faça denovo ou terá conflito. 

6. abra o git bash dentro da pasta mãe

7. abra acesso a pasta: git remote add origin link do repositorio

8. ainda não é possivel visualizar nada no github.

9. git remote add origin main

10. Pronto o repositório está pareado vscode/git/github

'''