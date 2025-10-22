CREATE DATABASE InventarioDB;
GO

USE InventarioDB;
GO


CREATE TABLE productos (
    codigo VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    stock INT NOT NULL,
    stock_minimo INT NOT NULL,
    stock_maximo INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    activo BIT DEFAULT 1  -- soft delete
);


CREATE TABLE movimientos (
    id INT IDENTITY PRIMARY KEY,
    codigo_producto VARCHAR(50),
    usuario_responsable VARCHAR(50),
    tipo VARCHAR(20),
    cantidad INT,
    motivo VARCHAR(200),
    stock_antes INT,
    stock_despues INT,
    monto_total DECIMAL(10,2),
    fecha_movimiento DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (codigo_producto) REFERENCES productos(codigo)
);


CREATE TABLE empleados (
    nombre_usuario VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    rut VARCHAR(12),
    celular VARCHAR(20),
    correo_electronico VARCHAR(50),
    genero VARCHAR(10),
    clave VARCHAR(MAX),  -- guardará hash de bcrypt
    cargo_trabajo VARCHAR(50)
);


SELECT * FROM empleados;
SELECT * FROM movimientos;
SELECT * FROM productos;