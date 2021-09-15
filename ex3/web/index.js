const express = require('express')
const os = require('os')
const mysql = require('mysql')
const app = express()

const connection = mysql.createConnection({
    host: "mysql-service",
    user: "root",
    password: "password",
}
)

app.get('/', (req, res) => {
    connection.connect()
        res.end("Bonjour tout le monde, je suis le conteneur id" + os.hostname() + ",je me suis connecté à la base de données")

    //res.end("Bonjour tout le monde, je suis le conteneur id" + os.hostname() + ",je me suis connecté à la base de données")

})

app.listen(3000, () => {
    console.log("Server web connected")
})