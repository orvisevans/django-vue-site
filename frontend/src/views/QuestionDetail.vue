<template>
  <div v-if="questionLoaded">
    <h3>{{ question.question_text }}</h3>
    <p class="date">{{ question.pub_date }}</p>
    <ul>
      <li v-for="choice in question.choices" :key="choice.id">
        {{ choice.choice_text }}
      </li>
    </ul>
  </div>
  <div v-else>
    <h3>Loading Question....</h3>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "QuestionSummary",
  data() {
    return {
      question: false,
    };
  },
  created() {
    const id = this.$route.params.id;
    const url = `http://localhost:8000/polls/api/questions/${id}?expand=choices`;
    axios
      .get(url)
      .then((response) => (this.question = response.data))
      .catch((err) => console.error(err));
  },
  computed: {
    questionLoaded() {
      console.log(this.question);
      return Boolean(this.question);
    },
  },
};
</script>

<style scoped>
</style>
