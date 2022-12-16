# puzzle
## Q-Learning
### TD誤差によるQの更新
状態$s_0$から行動$a_0$により、報酬$r_0$を受け取って状態$s_1$に遷移したとき、行動価値関数$Q(state, action)$の値$Q(a_0, s_0)$は次のように更新される。
```math
Q(s_0, a_0) \rightarrow Q(s_0, a_0) + lr(r_0 + \gamma max_a(Q(s_1, a)) - Q(s_0, a_0))
```
$lr$: 学習率
$\gamma$: 割引率. 次の報酬の現在価値を算出

### $\varepsilon-Greedy$法
生存バイアスを軽減するために、確率$\varepsilon$を基準に探索or利用を選択する。

### 参考サイト
https://qiita.com/persimmon-persimmon/items/fe543be28efb284bc8b2