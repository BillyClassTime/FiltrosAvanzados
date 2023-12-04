-- SQLite
-- Crear la tabla 'ventas'
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY,
    producto TEXT,
    ciudad TEXT,
    cantidad INTEGER
);

-- Insertar datos en la tabla 'ventas'
INSERT INTO ventas (id, producto, ciudad, cantidad) VALUES
    (1, 'Nissan', 'Valencia', 10),
    (2, 'Nissan', 'Madrid', 5),
    (3, 'Nissan', 'Barcelona', 5),
    (4, 'Mazda', 'Valencia', 25),
    (5, 'Mazda', 'Madrid', 30),
    (6, 'Mazda', 'Barcelona', 20);

-- Crear la tabla 'productos'
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT
);

-- Insertar datos en la tabla 'productos'
INSERT INTO productos (id, nombre) VALUES
    (1, 'Nissan'),
    (2, 'Mazda');

-- Crear la tabla 'ciudades'
CREATE TABLE IF NOT EXISTS ciudades (
    id INTEGER PRIMARY KEY,
    nombre TEXT
);

-- Insertar datos en la tabla 'ciudades'
INSERT INTO ciudades (id, nombre) VALUES
    (1, 'Barcelona'),
    (2, 'Madrid'),
    (3, 'Valencia');
