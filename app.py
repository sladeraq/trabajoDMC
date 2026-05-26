import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones as lf

st.title("Mi Segunda aplicación en python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Carlos Carrillo")

st.sidebar.image("DMC.png")

sesion = st.sidebar.selectbox("Seleccione Menu", ["Home", "Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"] )
CheckButton = False

if sesion == "Home":
  st.write("Bienvenido al trabajo de Pytho")
  st.image("Python_logo.png" )
  st.write("Alumno: Samuel Ladera Quinto")
  st.write("Modulo: Python Fundamentos")
  st.write("---------------------------------")
  st.write("Tecnologia utilizadas: HTML")

if sesion == "Ejercicio 1":
  @st.dialog("Mensaje")
  def mostrar_popup():
    st.write("Contenido Registrado correctamente")

    if st.button("Cerrar"):
        st.rerun()
  
  st.write("Bienvenido al Ejercicio 1")
  st.image("Python_logo.png" )
  # Crear lista persistente
  if "datos" not in st.session_state:
    st.session_state.datos = []

    
  concepto = st.text_input("Ingrese Concepto",key="txtconcepto")
  movimiento = st.selectbox("Escoger Tipo de Movimiento", ["Ingreso", "Gasto"] , key="boxmovimiento")
  valor = st.number_input("Ingrese Valor", key="txtvalor")

  if st.button ("Registrar"):
    st.session_state.datos.append ([concepto, movimiento, valor])
    mostrar_popup()
    
  if st.button ("Generar Reporte"): 
    # Crear DataFrame
    df = pd.DataFrame(
        st.session_state.datos,
        columns=["Descripción", "Tipo", "Monto"]
    )
    st.write("Movimientos Registrados")
    st.table(df)
    st.divider()

    totalingresos = sum(
    fila[2]
    for fila in st.session_state.datos
    if fila[1] == "Ingreso"
    )
    
    st.write("TOTAL DE INGRESOS :", totalingresos)
    st.write("TOTAL DE GASTOS :")
    st.write("SALDO FINAL :")
    st.write("FLUJO DE CAJA : ")


elif sesion == "Sesión 2":
  st.write("Bienvenido la sesión 2")

  precio = st.number_input("Ingrese el precio del producto", min_value = 0 , max_value = 5000 , value = 1200)
  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100% ", min_value = 0 , max_value = 100 )

  precio_final_producto = precio - (precio*(descuento/100))

  st.write("El precio final del producto es: ", precio_final_producto  )


elif sesion == "Sesión 3":
  st.write("Bienvenido la sesión 3")
  
  fin_rango = st.slider("Selecione un valor",min_value = 0 , max_value=20, value =7 )

  arreglo = np.arange(0 , fin_rango)

  st.write(arreglo)

elif sesion == "Sesión 4":
   st.write("Bienvenido a la sesión 4")
   principal = st.number_input("Ingrese el monto del préstamo", value=1000)
   tasa_anual = st.number_input("Ingrese la tasa anual en decimal", value=0.1, min_value=0.0, max_value=1.0)
   anios = st.number_input("Ingrese el número de años del préstamo", value=1)
   pagos_anio = st.number_input("Ingrese la cantidad de pagos por año", value=12)
    
   cuota = round(lf.cuota_prestamo(principal, tasa_anual, anios, pagos_anio),2)
   st.write(f"El valor de la cuota es {cuota}")
