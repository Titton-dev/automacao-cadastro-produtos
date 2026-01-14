import time
import pyautogui
import pandas

#Link do sistema da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 0.5
#Passo 1: Abrir o navegador e entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("OBOHA000252    Hashtag pera Air")
pyautogui.press("enter")
time.sleep(2)
#Passo 2:Fazer login no sistema
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=594, y=405) #Clicar no campo de email
pyautogui.write("dinossaursoazul@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
#Passo 3: Importar a base de dados
tabela = pandas.read_csv("Projeto 1/produtos.csv")
print(tabela)
#Passo 4:Registrar um produto no sistema
for linha in tabela.index:
    pyautogui.click(x=601, y=285)

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("enter")  # REGISTRA O PRODUTO
    time.sleep(1)
    pyautogui.scroll(5000)  # VOLTA PARA O TOPO DA PÁGINA