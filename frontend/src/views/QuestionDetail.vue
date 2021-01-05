<template>
  <div v-if="questionLoaded">
    <h3>{{ question.question_text }}</h3>
    <p class="date">{{ question.pub_date }}</p>
    <ul>
      <li v-for="choice in question.choices" :key="choice.id">
        <button @click="voteFor(choice)">
          {{ choice.choice_text }}
        </button>
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
    axios
      .get(this.questionApiUrl)
      .then((response) => (this.question = response.data))
      .catch((err) => console.error(err));
  },
  computed: {
    questionLoaded() {
      console.log(this.question);
      return Boolean(this.question);
    },
    questionApiUrl() {
      const id = this.$route.params.id;
      return `http://localhost:8000/polls/api/questions/${id}/?expand=choices`;
    },
  },
  methods: {
    getChoiceUrl(id) {
      return `http://localhost:8000/polls/api/choices/${id}/`;
    },
    goToResults() {
      const routePath = `${this.$route.path}/results`;
      this.$router.push(routePath);
    },
    voteFor(choice) {
      const url = this.getChoiceUrl(choice.id);
      const newChoice = {
        ...choice,
        votes: choice.votes + 1,
      };
      axios
        .put(url, newChoice)
        .then(this.goToResults)
        .catch((err) => console.error(err));
    },
  },
};
</script>

<style scoped>
</style>
