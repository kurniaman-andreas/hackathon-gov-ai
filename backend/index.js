const express = require("express");
const cors = require("cors");
const { CosmosClient } = require("@azure/cosmos");

// Ganti dengan URI dan Primary Key dari Cosmos DB kamu
const endpoint = "https://fikrihackathon.documents.azure.com/";
const key =
  "yA7ZM2BpeVGBVlAs68Jyn7m2F27GCJGl8MXm4ExSOezC5fWHcWyyzc8pYucnMDkDEtyNZPOHuuiwACDblLzNow==";
const client = new CosmosClient({ endpoint, key });

const app = express();
const port = 3001; // Port backend, berbeda dari frontend

app.use(cors());

// Endpoint untuk mengambil data dari Cosmos DB
app.get("/api/data", async (req, res) => {
  const databaseId = "FikriDatabase"; // Ganti dengan database ID
  const containerId = "Fikri1"; // Ganti dengan container ID
  const container = client.database(databaseId).container(containerId);

  try {
    const { resources } = await container.items.readAll().fetchAll();
    res.json(resources);
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data");
  }
});

// Jalankan server
app.listen(port, () => {
  console.log(`Backend is running at http://localhost:${port}`);
});
