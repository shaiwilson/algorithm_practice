

# 0(n * n)
int a = 0;
for (i = 0; i < N; i++) {
    for (j = N; j > i; j--) {
        a = a + i + j;
    }
}

# first step : i = 0 runs for N times
# when i = 1, it runs for N - 1 times 
# when i = k, it runs for N - k times

# N + (N-1) + (N-2)
# N * (N + 1) / 2
# 1/2 * N ^ 2 + 1/2 * N