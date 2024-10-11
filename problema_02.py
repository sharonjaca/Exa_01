#------------------------
# Import libraries
#------------------------
import random

#----------------------------------------------------
# Initialize cube with hour and week constraints
#----------------------------------------------------
def iniCubo(cb, num_empleados, num_semanas):
    for fil in range(num_empleados):
        for col in range(6):  # Seis días de trabajo
            for pro in range(num_semanas):  # Número de semanas que tiene el mes
                cb[fil][col][pro] = random.randint(1, 12)  # Restricción de máximo 12 horas


#----------------------------------------------------
# Print cube of hours worked in table format
#----------------------------------------------------
def impCubo(cb, empleados, num_semanas):
    dias_semana = ['L', 'K', 'M', 'J', 'V', 'S']  # Días de la semana
    for fil in range(len(empleados)):
        print(f"Empleado: {empleados[fil]}")
        for sem in range(num_semanas):
            # Imprimir los encabezados de los días solo en la primera semana
            if sem == 0:
                print("Semana", end="   ")
                for dia in dias_semana:
                    print(f"{dia:>4}", end=" ")
                print()

            # Imprimir los datos de las horas trabajadas para la semana actual
            print(f"Semana {sem + 1}: ", end=" ")
            for col in range(6):  # Seis días de trabajo
                print(f"{cb[fil][col][sem]:>4}", end=" ")
            print()
        print('=====================================')


#----------------------------------------------------
# Calculate monthly salary of each employee with hour breakdown
#----------------------------------------------------
def calcularSalario(cubo, salarios, num_empleados, num_semanas):
    salarios_totales = []
    sub_total_normales = 0
    sub_total_extras = 0
    sub_total_bruto = 0
    resultado_detallado = []

    for fil in range(num_empleados):
        horas_normales_total = 0
        horas_extras_total = 0
        salario_bruto = 0

        for sem in range(num_semanas):
            for col in range(6):
                horas_trabajadas = cubo[fil][col][sem]


                if horas_trabajadas > 8:
                    horas_extras = horas_trabajadas - 8
                    horas_normales = 8
                else:
                    horas_normales = horas_trabajadas
                    horas_extras = 0


                horas_normales_total += horas_normales
                horas_extras_total += horas_extras


                salario_bruto += (horas_normales * salarios[fil]) + (horas_extras * salarios[fil] * 1.5)

        # ----------------------------------------------------
        # # Save the breakdown for each employee
        # ----------------------------------------------------
        resultado_detallado.append({
            "empleado": fil,
            "horas_normales": horas_normales_total,
            "valor_hora_normal": salarios[fil],
            "monto_horas_normales": horas_normales_total * salarios[fil],
            "horas_extras": horas_extras_total,
            "valor_hora_extra": salarios[fil] * 1.5,
            "monto_horas_extras": horas_extras_total * salarios[fil] * 1.5,
            "salario_bruto": salario_bruto
        })


        sub_total_normales += horas_normales_total * salarios[fil]
        sub_total_extras += horas_extras_total * salarios[fil] * 1.5
        sub_total_bruto += salario_bruto

    return resultado_detallado, sub_total_normales, sub_total_extras, sub_total_bruto


# ----------------------------------------------------
# Print spreadsheet with detailed format
# Auxiliary function
# ----------------------------------------------------
def imprimirFila(empleado, horas_normales, valor_hora_normal, monto_horas_normales,
                 horas_extras, valor_hora_extra, monto_horas_extras, salario_bruto):
    print(f"{empleado:<10} {horas_normales:<15} {valor_hora_normal:<10} {monto_horas_normales:<12} "
          f"{horas_extras:<13} {valor_hora_extra:<10} {monto_horas_extras:<12} {salario_bruto:<10}")


# ----------------------------------------------------
# Function to print the detailed spreadsheet
# ----------------------------------------------------
def imprimirPlanillaDetallada(empleados, detalles_salarios, sub_total_normales, sub_total_extras, sub_total_bruto):
    print("\n--- Nómina Detallada de Empleados ---")


    print(
        f"{'Empleado':<10} {'Horas Normales':<15} {'Valor':<10} {'Monto ¢':<12} {'Horas Extras':<13} {'Valor':<10} {'Monto ¢':<12} {'Bruto ¢':<10}")


    for detalle in detalles_salarios:
        empleado = empleados[detalle['empleado']]
        imprimirFila(
            empleado,
            detalle['horas_normales'],
            detalle['valor_hora_normal'],
            detalle['monto_horas_normales'],
            detalle['horas_extras'],
            detalle['valor_hora_extra'],
            detalle['monto_horas_extras'],
            detalle['salario_bruto']
        )


    print("\nSubtotales:")
    print(f"{' ':<25} {sub_total_normales:<12} {' ':<25} {sub_total_extras:<12} {sub_total_bruto:<10}")
    print("=====================================")


# ----------------------------------------------------
# Start the program
# ----------------------------------------------------
def main():
    # Obtener número de empleados y semanas
    num_empleados = int(input("Ingrese el número de empleados: "))
    num_semanas = int(input("Ingrese el número de semanas del mes (4 o 5): "))


    empleados = []
    for i in range(num_empleados):
        nombre = input(f"Ingrese el nombre del empleado {i + 1}: ")
        empleados.append(nombre)


    salarios = []
    for i in range(num_empleados):
        salario = float(input(f"Ingrese el salario por hora de {empleados[i]}: "))
        salarios.append(salario)

    # Declare dynamic data cube [num_employees][6 days][num_weeks]
    cubo = [[[0 for _ in range(num_semanas)] for _ in range(6)] for _ in range(num_empleados)]

    # Initialize cube with hours worked data
    iniCubo(cubo, num_empleados, num_semanas)

    # Print the cube (hour record)
    impCubo(cubo, empleados, num_semanas)

    # Calculate monthly salary of each employee with details
    detalles_salarios, sub_total_normales, sub_total_extras, sub_total_bruto = calcularSalario(cubo, salarios,
                                                                                               num_empleados,
                                                                                               num_semanas)

    # Print the payroll with detailed format
    imprimirPlanillaDetallada(empleados, detalles_salarios, sub_total_normales, sub_total_extras, sub_total_bruto)



if __name__ == "__main__":
    main()
