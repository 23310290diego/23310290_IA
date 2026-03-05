#2.1

# Imprime el texto pero NO hace salto de línea al final
# end="" evita que Python agregue el salto de línea automático
print("Mi nombre es ", end="")

# Continúa imprimiendo en la misma línea
print("Monty Python.")

# Imprime varias palabras separadas por guiones
# sep="-" cambia el separador por defecto (que es espacio)
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")



# Imprime las palabras separadas por "_"
# sep="_" cambia el separador por defecto (espacio)
# end="*" evita el salto de línea y agrega un asterisco al final
print("Mi", "nombre", "es", sep="_", end="*")

# Imprime las palabras separadas por "*"
# sep="*" coloca asteriscos entre las palabras
# end="*\n" agrega un asterisco extra y luego un salto de línea
print("Monty", "Python.", sep="*", end="*\n")


#2.1.12
# Imprime tres palabras separadas por "***"
# sep="***" cambia el separador por defecto (espacio)
# end="..." evita el salto de línea y agrega "..." al final
print("Programming", "Essentials", "in", sep="***", end="...")

# Esta impresión continúa en la misma línea
# porque la instrucción anterior no hizo salto de línea
print("Python")



#2.1.13
# Flecha doble tamaño y duplicada lado a lado
# Se usa un solo print()
# "\n" crea saltos de línea
# "texto" * 2 duplica cada línea horizontalmente
print(
("        *        " * 2) + "\n" +
("       * *       " * 2) + "\n" +
("      *   *      " * 2) + "\n" +
("     *     *     " * 2) + "\n" +
("    *       *    " * 2) + "\n" +
("   *         *   " * 2) + "\n" +
("  *           *  " * 2) + "\n" +
(" *             * " * 2) + "\n" +
("******     ******" * 2) + "\n" +
("     *     *     " * 2) + "\n" +
("     *     *     " * 2) + "\n" +
("     *     *     " * 2) + "\n" +
("     *     *     " * 2) + "\n" +
("     *     *     " * 2) + "\n" +
("     *     *     " * 2) + "\n" +
("     *******     " * 2)
)


