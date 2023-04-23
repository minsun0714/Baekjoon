const inputFileName =
  process.platform === "linux" ? "/dev/stdin" : "example.txt";

const input = require("fs")
  .readFileSync(inputFileName)
  .toString()
  .trim()
  .split("\n")
  .map((r) => r.split(" ").map(Number));

const [[V, E], [K], ...nodes] = input;

let graph = Array.from({ length: V + 1 }, () => []);
let distance = Array.from({ length: V + 1 }, () => Infinity);

class PriorityQueue {
  constructor() {
    this.heap = [];
  }

  enqueue(item, priority) {
    const node = { item, priority };
    let i = 0;

    while (i < this.heap.length && this.heap[i].priority <= priority) {
      i++;
    }

    this.heap.splice(i, 0, node);
  }

  dequeue() {
    return this.heap.shift();
  }

  get length() {
    return this.heap.length;
  }
}

for (let [u, v, w] of nodes) {
  graph[u].push([v, w]);
}

function dijkstra(startNode) {
  const pq = new PriorityQueue();
  pq.enqueue(startNode, 0);
  distance[startNode] = 0;

  while (pq.length) {
    const { item: node, priority: dist } = pq.dequeue();

    const adj = graph[node];
    for (let i = 0; i < adj.length; i++) {
      let cost = dist + adj[i][1];

      if (cost < distance[adj[i][0]]) {
        distance[adj[i][0]] = cost;
        pq.enqueue(adj[i][0], cost);
      }
    }
  }
}

dijkstra(K);

for (let i = 1; i < V + 1; i++) {
  console.log(distance[i] === Infinity ? "INF" : distance[i]);
}
