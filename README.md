# Práctica de introducción a GitHub

Este repositorio se utilizará para aprender el flujo básico de Git y GitHub:

1. Clonar un repositorio.
2. Revisar sus archivos.
3. Realizar una modificación sencilla.
4. Comprobar los cambios con `git status` y `git diff`.
5. Crear un commit.
6. Publicar el cambio con `git push`.

## Primera actividad

Abra el archivo `participantes.md` y agregue:

- Su nombre.
- El programa académico al que pertenece.
- Una frase corta sobre lo que espera aprender de GitHub.

Después ejecute:

```bash
git status
git diff
git add participantes.md
git commit -m "Agrega participante Nombre"
git push origin main
```

## Segunda actividad opcional

Modifique uno de los valores del archivo `datos/mediciones.csv`. Luego ejecute
el programa:

```bash
python src/resumen.py
```

El programa calcula el promedio de las mediciones registradas.

## Estructura

```text
repositorio_practica_github/
├── README.md
├── participantes.md
├── datos/
│   └── mediciones.csv
└── src/
    └── resumen.py

- Su nombre. Dayren Barreto
- El programa académico al que pertenece. Ingenieria Ambiental
- Una frase corta sobre lo que espera aprender de GitHub. Si
```
