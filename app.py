import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones as lf

st.title("Trabajo de Python")
st.image("banner.png" )

#st.sidebar.title("Parámetros")

st.sidebar.image("menu.jpg")

sesion = st.sidebar.selectbox("Seleccione Menu", ["Home", "Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"] )
CheckButton = False

if sesion == "Home":
  st.write("Bienvenido al trabajo de Pytho")

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

    totalgastos = sum(
    fila[2]
    for fila in st.session_state.datos
    if fila[1] == "Gasto"
    )
    
    SaldoFinal = totalingresos - totalgastos
    if SaldoFinal > 0:
      Flujo= "A FAVOR"
    else:
      Flujo= "EN CONTRA"
    
    st.write("TOTAL DE INGRESOS :", totalingresos)
    st.write("TOTAL DE GASTOS :", totalgastos)
    st.write("SALDO FINAL :", SaldoFinal)
    st.markdown(
      f"FLUJO DE CAJA : <span style='color:red'>{Flujo}</span>",
      unsafe_allow_html=True
    )

elif sesion == "Ejercicio 2":
    
  st.divider()
  
  #aqui se crra array
  if "productos" not in st.session_state:
  
      st.session_state.productos = np.empty(
          (0, 5),
          dtype=object
      )
  
  # el formulario
  st.subheader("Formulario de Registro")
  
  producto = st.text_input("Ingrese Producto")
  categoria = st.selectbox("Seleccione Categoría",["Tecnología","Ropa","Hogar","Alimentos"])
  precio = st.number_input("Ingrese Precio",min_value=0.0,step=1.0)
  cantidad = st.number_input("Ingrese Cantidad",min_value=1,step=1)
  
  # calcular TOTAL
  total = precio * cantidad
  
  st.write("TOTAL :", total)
  
  st.divider()
  
  # boton
  if st.button("Agregar Registro"):
  
      # NUEVA FILA
      nueva_fila = np.array([[producto,categoria,precio,cantidad,total]],dtype=object)
  
      # AGREGAR AL ARRAY
      st.session_state.productos = np.vstack(
          (
              st.session_state.productos,
              nueva_fila
          )
      )
  
      st.success("Registro agregado correctamente")
  
  # convertir a DATAFRAME
  df = pd.DataFrame(
      st.session_state.productos,
      columns=[
          "Producto",
          "Categoría",
          "Precio",
          "Cantidad",
          "Total"
      ]
  )
  
  # muestra la TABLA
  st.write("DataFrame Actualizado")
  
  st.dataframe(df)
  
  # otros calculos
  if len(df) > 0:
  
      st.divider()
  
      total_ventas = df["Total"].astype(float).sum()
  
      st.markdown(
          f"""
          <h4 style='color:green'>
          TOTAL GENERAL: S/. {total_ventas}
          </h4>
          """,
          unsafe_allow_html=True
      )


elif sesion == "Ejercicio 3":
    
    # importa la FUNCION
    from libreria_funciones_proyecto1 import (
        calcular_almacenamiento_respaldo
    )
    
    # TITULO
    st.title("Proyecto – Uso de Librería de Funciones")
    
    st.divider()
    
    # historico
    if "historico" not in st.session_state:
        st.session_state.historico = []
    
    # selector  DE FUNCION
    funcion = st.selectbox(
        "Seleccione Función",["Calcular Almacenamiento de Respaldo","Otras Funciones"])
    
    st.divider()
    
    # parametros
    st.subheader("Ingreso de Parámetros")
    
    numero_usuarios = st.number_input(
        "Número de Usuarios",
        min_value=1,
        step=1
    )
    
    archivos_por_usuario = st.number_input(
        "Archivos por Usuario",
        min_value=1,
        step=1
    )
    
    tamano_promedio_mb = st.number_input(
        "Tamaño Promedio por Archivo (MB)",
        min_value=0.1,
        step=0.1
    )
    
    factor_respaldo = st.number_input(
        "Factor de Respaldo",
        min_value=1.0,
        step=0.1
    )
    
    st.divider()
    
    # boton
    if st.button("Ejecutar Función"):
    
        # ejecutar la FUNCION
        resultado = calcular_almacenamiento_respaldo(
            numero_usuarios,
            archivos_por_usuario,
            tamano_promedio_mb,
            factor_respaldo
        )
    
        # mostrar los RESULTADOS
        st.subheader("Resultado")
    
        st.write(
            "Almacenamiento Estimado MB :",
            resultado["almacenamiento_estimado_mb"]
        )
    
        st.write(
            "Almacenamiento Estimado GB :",
            resultado["almacenamiento_estimado_gb"]
        )
    
        # guardar HISTORICO
        st.session_state.historico.append([
            numero_usuarios,
            archivos_por_usuario,
            tamano_promedio_mb,
            factor_respaldo,
            resultado["almacenamiento_estimado_mb"],
            resultado["almacenamiento_estimado_gb"]
        ])
    
    # DATAFRAME historico
    df = pd.DataFrame(
        st.session_state.historico,
        columns=[
            "Usuarios",
            "Archivos x Usuario",
            "Tamaño MB",
            "Factor Respaldo",
            "Resultado MB",
            "Resultado GB"
        ]
    )
    
    st.divider()
    
    # mostrar la TABLA
    st.subheader("Histórico de Resultados")
    
    st.dataframe(df)

elif sesion == "Ejercicio 4":
  
  # importar CLASE
  from libreria_clases_proyecto1 import Servidor
  
  # titulo
  st.subheader("Proyecto CRUD con Clases")
  
  st.divider()
  
  # SESSION STATE
  if "servidores" not in st.session_state:
      st.session_state.servidores = []
  
  # creacion de tabs 
  tab1, tab2, tab3, tab4 = st.tabs([
      "Crear",
      "Visualizar",
      "Actualizar",
      "Eliminar"
  ])
  
  with tab1:
  
      st.markdown("**Crear Nuevo Servidor**")
      nombre = st.text_input("Nombre Servidor")
  
      tiempo_total = st.number_input(
          "Tiempo Total Horas",
          min_value=1.0
      )
  
      tiempo_caida = st.number_input(
          "Tiempo Caída Horas",
          min_value=0.0
      )
  
      almacenamiento_total = st.number_input(
          "Almacenamiento Total GB",
          min_value=1.0
      )
  
      almacenamiento_usado = st.number_input(
          "Almacenamiento Usado GB",
          min_value=0.0
      )
  
      if st.button("Guardar Servidor"):
  
          try:
  
              servidor = Servidor(
                  nombre,
                  tiempo_total,
                  tiempo_caida,
                  almacenamiento_total,
                  almacenamiento_usado
              )
  
              resumen = servidor.resumen()
  
              st.session_state.servidores.append(resumen)
  
              st.success("Servidor registrado correctamente")
  
          except Exception as e:
  
              st.error(str(e))
  
  with tab2:
  
      st.subheader("Listado de Servidores")
  
      if len(st.session_state.servidores) > 0:
  
          df = pd.DataFrame(
              st.session_state.servidores
          )
  
          st.dataframe(df)
  
      else:
  
          st.warning("No existen registros")
  
  with tab3:
  
      st.subheader("Actualizar Registro")
  
      if len(st.session_state.servidores) > 0:
  
          nombres = [
              s["servidor"]
              for s in st.session_state.servidores
          ]
  
          servidor_select = st.selectbox(
              "Seleccione Servidor",
              nombres
          )
  
          nuevo_estado = st.selectbox(
              "Nuevo Estado",
              [
                  "Óptimo",
                  "Advertencia",
                  "Crítico"
              ]
          )
  
          if st.button("Actualizar"):
  
              for s in st.session_state.servidores:
  
                  if s["servidor"] == servidor_select:
  
                      s["estado"] = nuevo_estado
  
              st.success("Registro actualizado")
  
      else:
  
          st.warning("No existen registros")
  
  with tab4:
  
      st.subheader("Eliminar Registro")
  
      if len(st.session_state.servidores) > 0:
  
          nombres = [
              s["servidor"]
              for s in st.session_state.servidores
          ]
  
          eliminar_servidor = st.selectbox(
              "Seleccione Servidor a Eliminar",
              nombres
          )
  
          if st.button("Eliminar"):
  
              st.session_state.servidores = [
                  s
                  for s in st.session_state.servidores
                  if s["servidor"] != eliminar_servidor
              ]
  
              st.success("Registro eliminado")
  
      else:
  
          st.warning("No existen registros")
        
