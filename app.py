import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones as lf

st.title("Trabajo de Python")

#st.sidebar.title("Parámetros")

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
  
  # CREAR ARRAY PERSISTENTE
  if "productos" not in st.session_state:
  
      st.session_state.productos = np.empty(
          (0, 5),
          dtype=object
      )
  
  # FORMULARIO
  st.subheader("Formulario de Registro")
  
  producto = st.text_input("Ingrese Producto")
  categoria = st.selectbox("Seleccione Categoría",["Tecnología","Ropa","Hogar","Alimentos"])
  precio = st.number_input("Ingrese Precio",min_value=0.0,step=1.0)
  cantidad = st.number_input("Ingrese Cantidad",min_value=1,step=1)
  
  # CALCULAR TOTAL
  total = precio * cantidad
  
  st.write("TOTAL :", total)
  
  st.divider()
  
  # BOTON
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
  
  # CONVERTIR A DATAFRAME
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
  
  # MOSTRAR TABLA
  st.write("DataFrame Actualizado")
  
  st.dataframe(df)
  
  # CALCULOS OPCIONALES
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
    
    # IMPORTAR FUNCION
    from libreria_funciones_proyecto1 import (
        calcular_almacenamiento_respaldo
    )
    
    # TITULO
    st.title("Proyecto – Uso de Librería de Funciones")
    
    st.divider()
    
    # HISTORICO
    if "historico" not in st.session_state:
        st.session_state.historico = []
    
    # SELECTOR DE FUNCION
    funcion = st.selectbox(
        "Seleccione Función",["Calcular Almacenamiento de Respaldo","Otras Funciones"])
    
    st.divider()
    
    # PARAMETROS
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
    
    # BOTON
    if st.button("Ejecutar Función"):
    
        # EJECUTAR FUNCION
        resultado = calcular_almacenamiento_respaldo(
            numero_usuarios,
            archivos_por_usuario,
            tamano_promedio_mb,
            factor_respaldo
        )
    
        # MOSTRAR RESULTADOS
        st.subheader("Resultado")
    
        st.write(
            "Almacenamiento Estimado MB :",
            resultado["almacenamiento_estimado_mb"]
        )
    
        st.write(
            "Almacenamiento Estimado GB :",
            resultado["almacenamiento_estimado_gb"]
        )
    
        # GUARDAR HISTORICO
        st.session_state.historico.append([
            numero_usuarios,
            archivos_por_usuario,
            tamano_promedio_mb,
            factor_respaldo,
            resultado["almacenamiento_estimado_mb"],
            resultado["almacenamiento_estimado_gb"]
        ])
    
    # DATAFRAME HISTORICO
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
    
    # MOSTRAR TABLA
    st.subheader("Histórico de Resultados")
    
    st.dataframe(df)

elif sesion == "Ejercicio 4":
  import streamlit as st
  import pandas as pd
  
  # IMPORTAR CLASE
  from libreria_clases_proyecto1 import Servidor
  
  # TITULO
  st.title("Proyecto CRUD con Clases")
  
  # DESCRIPCION
  st.markdown("""
  Aplicación desarrollada usando Programación Orientada a Objetos.
  
  La app permite:
  
  - Crear servidores
  - Visualizar registros
  - Actualizar registros
  - Eliminar registros
  - Calcular disponibilidad y estado
  
  Usando la clase:
  
  - Servidor
  """)
  
  st.divider()
  
  # SESSION STATE
  if "servidores" not in st.session_state:
      st.session_state.servidores = []
  
  # TABS
  tab1, tab2, tab3, tab4 = st.tabs([
      "Crear",
      "Visualizar",
      "Actualizar",
      "Eliminar"
  ])
  
  # ======================================================
  # TAB CREAR
  # ======================================================
  
  with tab1:
  
      st.subheader("Crear Nuevo Servidor")
  
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
  
  # ======================================================
  # TAB VISUALIZAR
  # ======================================================
  
  with tab2:
  
      st.subheader("Listado de Servidores")
  
      if len(st.session_state.servidores) > 0:
  
          df = pd.DataFrame(
              st.session_state.servidores
          )
  
          st.dataframe(df)
  
      else:
  
          st.warning("No existen registros")
  
  # ======================================================
  # TAB ACTUALIZAR
  # ======================================================
  
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
  
  # ======================================================
  # TAB ELIMINAR
  # ======================================================
  
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
        
