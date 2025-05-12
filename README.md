![Logótipo do NEIIST](https://neiist.tecnico.ulisboa.pt/static/media/neiist_logo.5b6bbd8f2f7eb5ee5200.png)
# Workshop Git - NEIIST

## 1 · Fork do repositório

1. Abre o repositório oficial no GitHub  
2. Clica no botão ```Fork``` (canto superior direito).
3. Escolhe **a tua conta** como destino.

---

## 2 · Clonar o teu fork localmente

No terminal (onde quiseres guardar o projecto):

```bash
git clone https://github.com/<o_teu_utilizador>/workshop-git.git # ou com ssh key
cd workshop-git
```

## 3 · Fazer git pull

## 4 · Criar branches para cada feature
```bash 
git checkout -b <branch_name>
```

## 5.1 · Implementar funções na diretoria ```functions```:
- [ ] multiplication
- [ ] division
- [ ] max
- [ ] min
- [ ] avg

## 5.2 · Adicionar funções novas à lista e ao parser em ```main.py```:
- [ ] multiplication
- [ ] division
- [ ] max
- [ ] min
- [ ] avg
      
## 6 · Fazer add, commit, push
```bash 
git add -A  # recomenda-se sempre a fazer git status para ver se há algo fora do comum
git commit -m "feat: Implemented <feature>"
git push
# caso o branch não esteja na núvem fazer:
git push --set-upstream origin <branch_name>
```
## 7 · Merge && Resolver Conflitos
```bash
git pull
git checkout master ou main
git merge <branch_name>
```

## 8 · Adicionar testes das novas funcionalidades em ```tests/test_functions.py```:
- [ ] multiplication
- [ ] division
- [ ] max
- [ ] min
- [ ] avg

## 9 · Merge Final && Resolver Conflitos && Testar se está tudo OK


