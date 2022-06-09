#!/bin/bash
echo "Este script ira buscar informacoes sobre o SO. Executar?[s/n]"
read RESPOSTA
if [ $RESPOSTA != "s" ]
then
	echo "Execucao interrompida."
	exit
else
	echo "Buscando dados sobre o sistema."
	echo "..............................."
	echo "Data e Hora:"
	date
	echo "..............................."
	echo "Uso do Disco:"
	df
	echo "..............................."
	echo "Usuarios logados:"
	w
	echo "..............................."
fi

