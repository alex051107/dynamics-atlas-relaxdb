# 独立审查 2026-10-20 夜：在不在轨道上，方法是不是最优

审查人：Fable 子代理。只读锚点、产出文件和账本；没有读 `~/dynamics_atlas_eval/` 和任何 RelaxDB 标签文件；没有改任何文件。路径简写：`W/` = `~/dynamics_atlas_work/`，`T/` = `autoresearch/tasks/dynamics_atlas_stage1_loop_20261002/outputs/`。数字都是我从文件里数出来的。

## 一、偏航：核心对象还没有被按科学家的定义回答

**结论：方向回到了锚点，但"替代 APO 态"这个核心对象的答案仍然是按团队自己改写的规则给的，科学家一个字都没拿到。**

产出清点（`W/outputs/alt_apo_states_*.json`，去掉 `before_check` 副本）：42 个蛋白有替代 APO 行，yes 12、possible 11、unknown 19。按 合作的 NMR 科学家 的字面定义（慢到两个分开的峰），12 个 yes 里 `literal_two_peak` 写 "does not" 的 6 个（NtrC kex 13,580 s⁻¹、CRABP2、ARGKIN、BLVRB、CypA、RNase A），"cannot tell" 2 个（HtrA2 PDZ、VHR），"qualifies" 4 个（KRAS、RFAHTD、18092、27011）。这 4 个用 NMR 的眼光再看，只剩 1 个站得住：

- KRAS：作者说 intermediate-to-slow，CEST 有第二个 dip，³¹P 两套峰。成立。
- RFAHTD：分开的 B 态是去折叠态（zz 交换、300 ms）。这是折叠平衡，不是另一个折叠的 APO 构象。
- 18092：两套峰 5:1，但没有任何交换测量（无 zz、无 CEST、无速率）。静态异质性（脯氨酸顺反、His 标签、化学修饰）同样解释得通。
- 27011：作者的 "slow" 是 CPMG 意义上的；kex ≈ 3,500 s⁻¹ 对 ¹⁵N Δω 2–6 ppm（600 MHz 下约 770–2,300 rad/s），kex/Δω ≥ 1.5，是快到中间交换。

所以 42 个蛋白里，按科学家定义确认的替代 APO 态是 1 个。这不是失败，是正确的科学结果；问题是它写在一封六天没发出去的信里（`T/gina_review_round1/message_to_gina_DRAFT.md` 首行仍是 "Not sent"，v2 10-20 14:45）。

上次反思（`REFLECT_20261020_ZH.md`）三条调整的落实：

| 调整 | 状态 | 证据 |
|---|---|---|
| 1 当天发包 | 没做 | 草稿首行 "Not sent"；证据表 "Expert check: correct?" 列 1171/1171 空 |
| 2 unknown 归因、补 PDF | 做了一半，今晚在动 | `UNKNOWN_REASONS_ZH.md` 16:50；用户 20:02 放入 8 篇 PDF 加 SI（`W/sources_cache/PAPER_DOWNLOAD_MANIFEST_20261020.json`）；`W/ledger/run_pdf_reread.sh` 20:14 开始重读 11 篇 |
| 3 召回分两列、种子改为事后核对 | 分两列做了，种子没撤 | `W/ledger/batch3_F5_recall.json`：0.73 含种子、0.67 不含；但 `tools/screen_candidates.py`、`tools/promote_source_papers.py` 17:06 仍把来源论文无条件提到 A 级 |

最近 24 小时的工作分布（`find -mmin`）：109 个 case 目录里 43 个被动过；时间花在 E-030/E-031 修复和 F3 重测（18:37–18:59）、PDB 状态试做 7 个蛋白（19:06–19:22）、12 个工具文件改动。这些都在锚点范围内（9-29 合作的 NMR 科学家 的同源 PDB 补充要求、过滤坏实验），没有再碰 deep3（`W/deep3/` 最后写入 10-19）。偏航已经收住；没动的是"发出去"这一步。

判定层的填充率（`W/outputs/judgment_v0/`，42 个文件 882 条）：verdict unresolved 467（53%）、时间窗 undetermined 378（43%）、evidence_strength direct_measurement 269（30%）。证据表（`W/outputs/pilot133/evidence_rows.csv`，32 个蛋白 1171 行）：abstract_only 353（30%），Timescale 有内容 289（25%），Population 59（5%），Method 为 "other" 371（32%，最大的一类）。"更深不是更大"这句用户要求，在这些数字上还没有兑现。

## 二、方法是不是最优

**(a) 一读、双复读、裁定、起草、再审。** 架构合理，但它优化的是"行抄得对不对"，不是"这个蛋白有没有两套峰"。F2 每百行纠正 18.9（`BATCH3_FEASIBILITY_ZH.md`）说明 20 列的宽表本身是错误来源。更好的做法：针对核心问题只抽 6 个字段（参考态样品、kex、pB、Δω、作者的交换区间原话、是否观察到第二套峰/CEST dip/zz 交换峰），其余字段降为附录。成本：改一个提示词模板，重跑 42 个蛋白约一天（F4 中位 24 分钟）。证明更优的标准：同一批注错测试下纠正率降到 15 以下，且 yes/possible 判定不变。另一个方法学缺口：注错由 Claude 植入、Claude 评分、Claude 裁定（`batch3_F3_injection_score.json` 的 `scored_by`）。系统综述的做法是植入者不参与裁定；F3 的 20/20 重测里有 7 个是靠"两个读者都无法核实就送裁定"这条新规则抓到的，而这条规则在真实数据上触发 15%（233/1509），它换来的是裁定量不是召回。

**(b) 用 RelaxDB 来源论文做种子。** 作为先验没错，作为搜索输入它让召回率失去意义：第三批 10 个有来源 DOI 的蛋白里 8 个只经 `seed` 通道进来（`W/outputs/candidates/*.json`，seed 通道 46 条）。替代做法：种子改用 BMRB 条目自带的 primary citation（56 个数字编号条目都有，这是公开出处元数据，不是标签），召回只在非种子集上报。F5 现在的"外部清单"是 PDB 主引用加 UniProt 引用，再用标题正则判 NMR 类（`batch3_F5_recall.json` 的 `classification_note`），n=15；这不是召回金标准。真正的金标准只有一个来源：合作的 NMR 科学家 给两个蛋白的预期论文清单（草稿信第 4 条）。

**(c) 逐蛋白替代 APO 判定。** 现在的 yes 规则是"参考态有测到速率和布居的少数态"。这把 CPMG 看不见的态和两套峰看得见的态混在一个词里。应该分两列：`visible_minor_state`（两套峰、CEST 第二 dip、zz/EXSY 交换峰、峰倍增）和 `dispersion_only_minor_state`。字段已经存在（`literal_two_peak`、`regime`、`kex`、`pB`），拆列是一小时的工作，不需要重读。

**(d) PDB 映射。** `tools/pdb_states.py` 的闭合度轴对 AQADK/ARGKIN（9.7 Å）有效，对其余 5 个（两态只差 0.7–1.2 Å）信息量接近坐标误差，报告自己也这样写了。现成资源：PDBe-KB 构象聚类已经用了；CoDNaS 2.0（同一蛋白多构象体按配体、pH、温度分组，https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4809262/ ，站点是否在线未核实）可以替代自建的 apo/holo 分组。真正能把 NMR 少数态对到结构上的检验是化学位移：用候选结构预测位移（SHIFTX2 或 UCBShift），和 CPMG 的 Δω 符号与大小比对。报告的下一步已经写了这一条，它需要装软件（用户批准）。在那之前继续扩到更多蛋白，产出的只会是更多"没有 apo 结构落在另一态里"。

**(e) 从 BMRB 沉积数据出发。** 不可行：12 个条目的回读只有 T1/T2/NOE 三类（`W/outputs/deposition/*.json`）；BMRB 没有 CPMG 色散的专用类别，relax 软件的开发者 2014 年就找不到已沉积的 CPMG 例子（https://www.nmr-relax.com/api/4.0/specific_analyses.relax_disp.api-pysrc.html ）。文献线是对的起点。

## 三、流程抓不到的系统性错误

1. **交换区间来自作者的形容词，不是来自数字。** "slow" 在 CPMG 文献里常指 CPMG 窗口内偏慢，不是 合作的 NMR 科学家 的"两套峰"。流程没有算过 Δω/kex。证据就在替代 APO 行里：CheY D64 Δω 9.4 ppm、kex 96 s⁻¹（Table 2），按数字是慢交换，判定写 "cannot tell"；BLVRB G76 ΔωN 9.49 ppm 对 kex 1,088 s⁻¹，同样偏慢，判定写 "does not"；27011 反过来，作者说 slow，数字是快。检查方法：对所有印出 Δω 和 kex 的行（CheY Table 2、BLVRB SI Table S1、VHR、ARGKIN Table 1、RNase R33、27011）算 Δω(rad/s)/kex，和 `literal_two_peak` 逐条比对。只用现有文件。
2. **搜索是弛豫中心的，"看得见的少数态"藏在别的论文类型里。** 两套峰、zz 交换、峰倍增通常出现在归属论文、折叠论文和方法论文的正文，标题摘要不提（E-022 的 GB3 就是这个模式）。1171 行里带这类措辞的只有 46 行，其中 16 行 Method 是 "other"。检查：在 2801 条候选里按正文或 Europe PMC 全文检索 "zz-exchange / EXSY / two sets of peaks / doubling"，看有多少被摘要筛选判成 C 级。
3. **条目身份。** E-028 查出 5 张卡片的 UniProt 与序列几乎无重叠（17306、18092、50410、VCPTH 等）；18092 是 4 个"qualifies"之一，它的卡片 UniProt 是鼠白血病病毒多聚蛋白。数据库发布的第一条规则是稳定标识加来源，现在条目键混用 BMRB 数字号和项目名（AQADK_CPMG），行号在导出时重分配过一次（E-023）。检查：`W/ledger/card_identity_check_133.json` 的 33 个"非子串"条目逐一核对后再发任何表。

## 四、下一步做一件事，停三件事

**做：今晚把 CPMG-10 的包发出去。** 替代 APO 表拆成"可见少数态"和"仅色散少数态"两列；信里把"按字面只有 K-Ras"改成"按字面只有 K-Ras，RFaH 是去折叠态，eRF1 N 域是两套峰但无交换测量"；Papers_to_send 保留。PDF 已经到了，重读在跑，不必等它完成再发。

**停：** 不开第 4 批；来源 DOI 从搜索输入里撤出（`promote_source_papers.py`、E-029 规则停用）；PDB 映射不扩到剩下 3 个蛋白，先把 altloc 和化学位移比对这两个真正能改变答案的东西做出来。
