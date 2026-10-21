# 第二次独立反思：产出对照原始要求（2026-10-20）

对照物：`ORIGINAL_ASK_ZH.md` 及其引用的 9-17、9-29 两份会议源文件，加上用户 10-18、10-20 的三句话。只看产出文件和账本，不看团队的计划、报告和工作流文档；上一次反思只看了第五节的三条调整。所有数字由我从文件里数出来，路径写在每一行。工作目录简写 `W/` = `~/dynamics_atlas_work/`，任务目录简写 `T/` = `autoresearch/tasks/dynamics_atlas_stage1_loop_20261002/outputs/`。

## 一、逐项对照

| 锚点要求 | 状态 | 覆盖数字 | 一个具体例子 |
|---|---|---|---|
| 9-17：先专门做"替代 APO 状态" | 做了，但答案大多是"不知道" | 41 个蛋白有替代 APO 行（`W/outputs/alt_apo_states_v0.json` 10 个、`alt_apo_states_133_v0.json` 12 个、`alt_apo_states_batch3_G1–G8.json` 19 个）；判定 yes 12、possible 11、unknown 18 | CypA 判 yes，依据是 10 °C 下 2.0 ± 0.1% 的激发态（CYPA-r38），同一行的 `literal_two_peak` 字段写"does not"：作者说大多数残基是快交换，没有第二套峰 |
| 9-17：合作的 NMR 科学家 的定义，慢到能看见两个分开的峰 | 规则被改写了，改写后的"yes"和字面定义不一致 | 按字面定义 41 个里只有 4 个"qualifies"（KRAS、RFAHTD、18092，27011 只是用词上符合），11 个"does not"，26 个"cannot tell"。12 个 yes 里 6 个字面上"does not"，2 个"cannot tell" | 给 合作的 NMR 科学家 的草稿信自己承认："按我们的规则 10 个里 7 个 yes；按字面只有 K-Ras·GTP 一个"（`T/gina_review_round1/message_to_gina_DRAFT.md`） |
| 9-17：按定义扫 PDB 和 BMRB，agent 检索聚合，发布成数据库 | 文献线做了；PDB/BMRB 按定义扫描没做；数据库没有 | PDB 只拉了 10 个 CPMG 蛋白的结构文件（`W/structures/`，10-12 之后没动过）；BMRB 沉积数据回读只有 12 个条目（`W/outputs/deposition/`，10-17）；没有任何对外可用的数据库文件 | `W/structures/MANIFEST.md` 列了结构，之后没有一行分析产出 |
| 9-17：对上就映射状态，对不上就写"可能有替代构象，差异在这几个残基，依据是这批 NMR 测量" | 做了，格式对 | 41 行里 `structure_match` 非空 16，`fallback_annotation` 以"May have"开头 23 行、以"No alternate"开头 17 行 | CypA 退路标注："65–84 环可能有替代构象（D66、F67、T68、N71、G74、K76、S77、K82），依据 15N CPMG（doi:10.1038/nature04105）……" |
| 9-17：过滤做错的实验，比对实验/模拟条件是否可比 | 部分做了 | 证据表每行都有"Do not combine with / limits"列（1059/1060 填了）；缓冲液问题在草稿信里单列一段（CypA、CheY 磷酸盐，K-Ras EDTA） | 草稿信："只有 K-Ras-GDP 的次要态被标为疑似 EDTA/Mg 伪影" |
| 9-29：五样东西（残基、替代态结构、实验、时间尺度、布居） | 字段都有，数值大多数是空的 | 41 行里 kex 有数字 15、pB 有数字 13、残基有名 27、结构匹配 16；证据表 1060 行里"Timescale"有内容 250、"Population"有内容 58（`W/outputs/pilot133/evidence_rows.csv`） | 17306（设计锚蛋白）整行：kex "not measured"、pB "not measured"、残基 "none for µs-ms"、结构 `[]` |
| 9-29：方法范围（CPMG/CEST、晶体系综、时间分辨、FRET、EPR、MD、PDB 比较） | 做了 | 1060 行的 Method 分布：other 326、pdb_structure_comparison 193、md 134、nmr_spin_relaxation 124、exchange_broadening 79、relaxation_dispersion 75、ensemble_restraints 41、hdx_ms 28、fret 26、time_resolved 18、epr_deer 14 | 第三批 703 行里弛豫色散只有 26 行（3.7%），"other"242 行 |
| 9-29：先整理文献证据，暂不重新处理原始数据 | 文献线遵守；另开了一条原始数据线 | `W/deep3/` 有 ChemEx 拟合、SLURM 脚本（`deep3/slurm/chemex_array.sbatch`），最后写入 10-19 23:22，之后冻结 | 上次反思要求冻结；文件日期显示冻结生效 |
| 9-29：每个蛋白保留矛盾和不确定，不强行合成 | 做了 | 824 条判定里 unresolved 421（51%）、dynamic_in_window 318、no_evidence_in_window 68、not_measured 16、contested 1（`W/outputs/judgment_v0/*.json`，42 个蛋白） | CypA 的 caveats：apo 过程的个数有争议，"两组集体运动（r1）、一个全局过程（r38）、或逐残基连续分布（r10–r12）" |
| 9-29：顺序 10 → 133 → 更多；试点要帮助确定该收集什么、评估文献挖掘找到了什么 | 10 个做完；133 个做了 32 个；"评估找到了什么"没有外部答案 | 42/133 有判定，41/133 有替代 APO 行；第三批 20 个蛋白：unknown 13、possible 4、yes 2、缺 1（TRX） | 第三批预注册 F5"搜索召回 ≥ 70%"（`W/ledger/batch3_prereg.md`）在账本里没有任何结果数字（`batch3_run.log`、`batch3_rerun_run.log` 里搜不到 recall） |
| 9-29：合作的 NMR 科学家 提前拿论文、审查发现；试点后开会 | 没发生 | 给 合作的 NMR 科学家 的包做好了（工作簿 10 张表：替代 APO 10 行、证据 214 行、附录 383 行、判定 251 行、待送论文 112 篇），信第一行写"Not sent"；v1 草稿日期 10-14，v2 10-20 | 1060 行证据表的"Expert check: correct? (Y/N)"列 1060 个空 |
| 9-29 合作的 NMR 科学家 补充：从同源 PDB 里判断哪些是替代态 | 没做 | 草稿信："我们拉了 10 个蛋白的全部 PDB 条目，还没分析" | 同上 |
| 10-18 用户：要更深的版本，不是更大的版本 | 做的是更大的版本 | CPMG-10 证据 597 行全文占 84%（502/597）；第三批 703 行全文占 62%（438/703），摘要 265 行；第三批 20 个蛋白里 13 个 unknown | 待下载清单 7 篇全是 RelaxDB 取数据的原始论文，只读到摘要（`T/pilot133/PAPERS_TO_DOWNLOAD.md`） |
| 10-20 用户：稳定留下来做成 agent system，但优先保障科学性 | 工程在加，科学验收指标有一条未达标且继续推进 | 第三批 F2"每 100 行纠正 ≤ 15"：实际 132/703 = 18.8（`W/ledger/row_corrections.json`）；F3 注入测试账本里只有 10-17 的两个蛋白、单读者（`W/ledger/sr_dual/INJ_*_flags.json`），不是预注册的 20 个错误双读 | 账本最后 10 条错误 E-022–E-029 里 7 条状态是 open 或"implemented, not yet used" |
| 10-20 用户：审完后继续，扩大规模、验证可行性 | 规模扩了，可行性只验了一半 | F1 判定检查 20/20 通过、替代 APO 行 19/20；F4 每蛋白中位 22.5 分钟、全批 9.3 小时（`W/ledger/batch3_state.json`）；F7 非 unknown 占 6/20 = 30% | 通过的是"跑得完、跑得快"；没通过或没测的是"读得对、找得全" |

上次反思的三条调整：第 2 条（22 个蛋白各加替代 APO 行）做了，10 + 12 = 22 行，之后又加了 19 行；第 3 条（deep3 冻结）做了；第 1 条（本周把包发出）没做，草稿第六天仍是"Not sent"。

## 二、科学家实际拿到了什么

零。合作的 NMR 科学家 没有收到工作簿、没有收到论文清单、没有收到定义问题。从 9-29 到今天 21 天，锚点里"试点做完后开会"的条件一直没有触发，因为试点的结果没有离开过这台机器。

如果今天把包发出去，她拿到的是：10 个蛋白的替代 APO 行（7 个 yes），一封信坦白按她的字面定义只有 1 个成立，并请她二选一；214 行主证据加 383 行附录，每行带原文引句和链接；112 篇只读到摘要的论文清单；两个标签问题（CPMG 标签里"Y"算不算交换、CypA 标签来自哪个样品）。这个包的内容本身符合 9-29 要的格式：按蛋白、按区域残基、按实验、附出处、矛盾保留。

她拿不到的是：133 个蛋白里另外 32 个的结果（这部分还在自查，没有打包），任何 PDB/BMRB 扫描结果，任何同源结构判断，任何可以叫"数据库"的东西。

## 三、锚点没要、团队在做的事

1. **原始数据重拟合**（`W/deep3/`，ChemEx、bootstrap、SLURM 脚本，9.3 MB 的 detection_exclusions.csv）。9-29 会议明确说先不重新处理原始数据。已冻结，但在反思当天 22:54 之后还跑了半小时（C1_report 23:18、codex_c1.log 23:21）。
2. **对 RelaxDB 标签的逐残基对账**（`W/outputs/tracks/` 23 个文件、`tools/judgment_to_tracks.py`、`tools/qc_summary.py`）。锚点要的是替代状态证据，不是复现 RelaxDB 的标签；这条线把 RelaxDB 当成了评分器。
3. **流程工程**。`W/tools/` 33 个脚本 6048 行；10-20 一天改了 12 个。最大的几个：build_gina_table 636 行、loop_driver 551、second_read 436、campaign 433、screen_candidates 412、subagent_judge 403。账本里 8 份 Codex 执行单、13 份审阅文档、210 个 hook 会话、104 个 case 目录、v6_runs.jsonl 804 行。10-20 新增的 identity_preflight、promote_source_papers、unfilled_ab 都是修搜索管线，不产生答案。
4. **用 RelaxDB 元数据做搜索种子**（`W/config/relaxdb_source_dois.json` 60 条；`tools/auto_config.py` v6 把来源论文 DOI 并入种子；`tools/screen_candidates.py` E-029 规则把来源论文无条件提到 A 级）。这不泄露标签：`prompts/judgment_draft_v1.md` 第 20 行禁读的是标签文件，来源 DOI 是出处元数据。它破坏的是另一件事：召回率的测量。第三批 20 个蛋白里 10 个有来源 DOI，其中 8 个（50020、AZURIN、HTGFA、18306、TRX、RNASEHI、VL、UBE2G1）的来源论文进入候选表的唯一通道是 `seed`，只有 CD9K、CRABP2 是方法检索独立找到的（`W/outputs/candidates/*.json` 的 channel 字段）。也就是说，不靠 RelaxDB 提示，独立搜索在这 10 个蛋白上漏掉了 8 篇关键论文。v6 之后任何"找到了来源论文"的召回数字都是构造出来的；预注册 F5 用的 PDB/UniProt 清单本身也是候选通道（预注册自己写了"PDB 那一半部分循环"）。再往前看，9-17 的目标是扫 PDB 和 BMRB 里没有 RelaxDB 条目的蛋白，那里没有来源 DOI 可种，v6 的表现不会迁移过去。

## 四、最大的差距

**结果从未到达科学家，而决定 41 行判定意义的那个问题（"yes"按哪种读法）正躺在未发出的草稿里。** 10-19 的第一条调整就是本周发出，六天后它仍是"Not sent"，而同一周里替代 APO 行从 22 加到了 41，第三批跑了 9.3 小时，工具改了 12 个。团队用扩规模代替了等反馈。

两个后果已经在文件里：一是 12 个"yes"里 8 个按字面定义不成立，如果 合作的 NMR 科学家 选字面读法，这 41 行要重判一遍；二是第三批 13/20 是 unknown，主因是只读到摘要（第三批 38% 的行是摘要），而 7 篇最关键的来源论文都是 1993–1999 年的 Biochemistry，自动抓取拿不到，需要人去下载。这两件事都不是再跑一批能解决的，都需要一个人做一件事：发信、下 PDF。

用户 10-18 说要更深不要更大。CPMG-10 的全文率 84%，第三批 62%；每蛋白证据行从 60 行降到 35 行；弛豫色散行占比从 CPMG-10 的主体降到第三批的 3.7%。规模上去了，深度下来了。

## 五、结论：调整

1. **今天发出 CPMG-10 的包，不再改。** 信已经是第二版，内容够用。在 合作的 NMR 科学家 回答"按哪种读法"之前，不新开任何批次；团队的时间花在把 32 个 133 子集蛋白的包做成同样格式，等她第一轮意见回来一起发。
2. **把 18 个 unknown 变成有名字的原因，再补读 7 篇 PDF。** 每个 unknown 标明是"只有摘要"、"文献里没有这项测量"、还是"条目构建与文献不符"（E-028 那类）。先由人下载 `PAPERS_TO_DOWNLOAD.md` 的 7 篇，用"只重读这几篇"的方式更新判定；这 7 个蛋白重判之后，再决定第三批算不算可行。F2 未达标（18.8 > 15）照实写进第三批结论，不改阈值。
3. **召回率分两列报，来源 DOI 从搜索输入改成事后检查。** 现有的 v6 结果，凡是来源论文只经 `seed` 通道进来的（第三批 8/10），召回表里记作"RelaxDB 提示找到"，不记作"搜索找到"；独立召回 2/10 是现在的真实数字。往后把来源 DOI 留在搜索之后做核对（"我们自己找到了吗"），不再并入种子，否则这个流程到了没有 RelaxDB 的蛋白上没有可信的召回估计。真正的外部召回测试只有一个来源：草稿信第 4 条向 合作的 NMR 科学家 要的两个蛋白的预期论文清单，这又回到第 1 条。
