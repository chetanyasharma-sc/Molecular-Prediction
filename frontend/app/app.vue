<template>
  <main class="page">
  
    <section class="card">
      <h1>Molecular Solubility Predictor</h1>
      <p>Enter a SMILES string and get predicted log solubility.</p>

      <input
        v-model="smiles"
        placeholder="Example: CCO"
      />

     <button @click="predictSolubility">
  {{ loading ? "Predicting..." : "Predict Solubility" }}
</button>

      <div v-if="result" class="result">
  <h2>Prediction Result</h2>

  <div
    v-if="result.molecule_svg"
    class="molecule"
    v-html="result.molecule_svg"
  ></div>

  

  <p><strong>SMILES:</strong> {{ result.smiles }}</p>
  <p><strong>Predicted LogS:</strong> {{ result.predicted_solubility.toFixed(3) }}</p>
  <p><strong>Category:</strong> {{ result.category }}</p>
  <p><strong>Model:</strong> {{ result.model }}</p>

  <div v-if="result.descriptors" class="descriptor-grid">
    <div
      v-for="(value, key) in result.descriptors"
      :key="key"
      class="descriptor-card"
    >
      <span>{{ key.replaceAll('_', ' ') }}</span>
      <strong>{{ value }}</strong>
    </div>
  </div>

  <div v-if="result.lipinski" class="lipinski">
    <h3>Lipinski Rule of 5</h3>
    <p>
      <strong>Status:</strong>
      <span :class="result.lipinski.status === 'Pass' ? 'lipinski-pass' : 'lipinski-fail'">
        {{ result.lipinski.status }}
      </span>
    </p>

    <ul v-if="result.lipinski.violations.length">
      <li v-for="item in result.lipinski.violations" :key="item">
        {{ item }}
      </li>
    </ul>
  </div>

  <p class="note">{{ result.note }}</p>
</div>
      <p v-if="error" class="error">{{ error }}</p>
    </section>
  </main>
</template>

<script setup>
import { ref } from "vue"

const smiles = ref("")
const result = ref(null)
const error = ref("")
const loading = ref(false)

const predictSolubility = async () => {
  result.value = null
  error.value = ""
  loading.value = true

  try {
    const response = await fetch("https://ideal-doodle-pw9vq4wjr9g2475-8000.app.github.dev/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        smiles: smiles.value
      })
    })

    const data = await response.json()

    if (!response.ok) {
      error.value = data.detail || "Backend error"
      return
    }

    if (data.error) {
      error.value = data.error
      return
    }

    result.value = data
  } catch (err) {
    console.error(err)
    error.value = "Frontend could not connect to backend. Check backend server and CORS."
  } finally {
    loading.value = false
  }
}
</script>





<style>
.page {
  min-height: 100vh;
  background: #020617;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: Arial, sans-serif;
}
.chemistry-bg {
  position: fixed;
  inset: 0;
  z-index: 0;
  opacity: 0.08;

  background-image:
    url("/molecules/benzene.svg"),
    url("/molecules/caffeine.svg"),
    url("/molecules/quinazoline.svg");

  background-size: 220px;
  background-repeat: repeat;
}

.card {
  position: relative;
  z-index: 10;
}

.molecule {
  margin: 20px 0;
  padding: 16px;
  border-radius: 16px;
  background: white;
  display: flex;
  justify-content: center;
}

.card {
  width: 100%;
  max-width: 520px;
  padding: 32px;
  border-radius: 24px;
  background: rgba(15, 23, 42, 0.95);
  border: 1px solid rgba(148, 163, 184, 0.25);
}

input {
  width: 100%;
  padding: 14px;
  margin: 20px 0;
  border-radius: 12px;
  border: 1px solid #334155;
  background: #020617;
  color: white;
  font-size: 16px;
}

button {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 12px;
  background: linear-gradient(90deg, #06b6d4, #6366f1);
  color: white;
  font-weight: bold;
  cursor: pointer;
}

.result {
  margin-top: 24px;
  padding: 18px;
  border-radius: 16px;
  background: rgba(8, 47, 73, 0.5);
}

.note {
  color: #94a3b8;
  font-size: 13px;
}

.error {
  color: #f87171;
}



.descriptor-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-top: 20px;
}

.descriptor-card {
  padding: 12px;
  border-radius: 12px;
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.2);
}

.descriptor-card span {
  display: block;
  font-size: 12px;
  color: #94a3b8;
}

.descriptor-card strong {
  color: white;
}

.lipinski {
  margin-top: 20px;
  padding: 16px;
  border-radius: 14px;
  background: rgba(21, 128, 61, 0.15);
}
</style>