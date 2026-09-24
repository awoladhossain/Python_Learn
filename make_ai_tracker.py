"""
AI Engineer Transition Tracker — 6 Month Deep-Dive Plan (v2)
Generates: AI_Engineer_6Month_DeepDive.xlsx
Includes: Conditional Formatting, AutoFilter, Improved Week 25/26 content
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

# ---------- Styles ----------
HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
SUBHEADER_FILL = PatternFill("solid", fgColor="D9E1F2")
SUBHEADER_FONT = Font(bold=True, color="1F4E78", size=11)
TITLE_FONT = Font(bold=True, size=16, color="1F4E78")
SUBTITLE_FONT = Font(italic=True, size=11, color="595959")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)

# Conditional formatting fills
DONE_FILL = PatternFill("solid", fgColor="C6EFCE")        # green
DONE_FONT = Font(color="006100")
PROGRESS_FILL = PatternFill("solid", fgColor="FFEB9C")    # yellow
PROGRESS_FONT = Font(color="9C6500")
NOT_STARTED_FILL = PatternFill("solid", fgColor="F2F2F2") # grey
NOT_STARTED_FONT = Font(color="808080")

# ---------- SYLLABUS DATA (26 weeks, improved Week 25/26) ----------
SYLLABUS = [
    (1,1,"P1 · Python+Math","Python for Production AI + NumPy/Pandas Deep-Dive",
     "Comprehensions, generators, decorators, context managers, *args/**kwargs, type hints, dataclasses, Pydantic v2, uv/poetry envs, project layout (src/, tests/), logging, typer CLI. NumPy: ndarray internals, broadcasting, strides, views vs copies, einsum. Pandas: loc/iloc, groupby-agg, merge/join, pivot, resample, category dtype, chunking.",
     "Fluent Python Ch.1-5,17 | NumPy absolute beginners | Pandas intro tutorials | Real Python: decorators, generators, typing",
     "Build reusable package data_utils/ with load_csv, clean, summary, plot_distribution — type hints + tests. Push to GitHub.",
     "Python generator কী? Decorator লিখে দেখাও। 10M row Pandas-এ কীভাবে handle করবে?"),
    (2,1,"P1 · Python+Math","Linear Algebra + Calculus for DL",
     "Vectors, matrices, matmul, dot product, transpose, inverse, determinant, eigen decomposition, SVD, norms (L1/L2/Frobenius), Jacobian, Hessian concept. Calculus: derivative rules, chain rule, partial derivative, gradient, backprop derivation from scratch, numerical vs analytical gradient.",
     "3Blue1Brown Essence of Linear Algebra | 3Blue1Brown Essence of Calculus | Khan Academy | Karpathy micrograd video",
     "NumPy দিয়ে from scratch: matmul, dot, svd (power iteration), gradient_descent. Notebook-এ backprop chain rule দিয়ে 2-layer MLP derive।",
     "Backprop-এ chain rule কোথায়? SVD কী কাজে লাগে? Gradient vanishing কেন?"),
    (3,1,"P1 · Python+Math","Probability, Statistics, Optimization",
     "Random variables, PMF/PDF/CDF, expectation, variance, covariance, Bayes theorem, MLE vs MAP, Gaussian/Bernoulli/Categorical/Poisson, CLT, hypothesis testing, p-value, A/B test, confidence interval. Optimization: convex vs non-convex, SGD/Momentum/RMSProp/Adam/AdamW, LR schedules (cosine, warmup), Newton/L-BFGS concept.",
     "StatQuest: Probability, Bayes, MLE | Probabilistic ML (Murphy) Ch.2-4 free PDF | Distill.pub 'Why Momentum Really Works'",
     "Notebook: A/B test simulate করে p-value + CI বের করা। Adam optimizer নিজে লিখে 1D function minimize।",
     "Bayes theorem দিয়ে spam filter বানাও। Adam আর SGD-এর পার্থক্য? p-value কী?"),
    (4,1,"P1 · Python+Math","Data Wrangling, EDA, Feature Engineering (Data-Centric AI)",
     "Missing data (MCAR/MAR/MNAR), imputation, outlier detection (IQR, z-score, Isolation Forest), encoding (one-hot, ordinal, target, embeddings), scaling, feature interactions, polynomial, leakage detection, imbalance (SMOTE, class weights). EDA: distributions, correlation, mutual info, PCA/t-SNE/UMAP, ydata-profiling.",
     "Kaggle Learn: Data Cleaning + Feature Engineering | Designing ML Systems (Chip Huyen) Ch.3-4 | Andrew Ng Data-Centric AI talk",
     "Messy real dataset (NYC Taxi/House Prices): load → clean → FE → EDA report → saved clean data. GitHub push।",
     "Data leakage কী? Imbalanced data-তে কী করবে? Feature engineering-এর উদাহরণ?"),
    (5,2,"P2 · Classical ML","Supervised Learning I (Regression + Classification)",
     "Linear regression (normal eq + GD), logistic regression, Ridge/Lasso/ElasticNet, bias-variance, train/val/test, k-fold + stratified CV, metrics (MSE, MAE, R², accuracy, precision, recall, F1, ROC-AUC, PR-AUC, confusion matrix).",
     "Andrew Ng ML Specialization Course 1 | scikit-learn supervised learning guide | StatQuest: ROC/AUC, cross-validation",
     "Tabular dataset-এ ৩টা regression + ৩টা classification model — comparison report (metrics + plots).",
     "Precision vs recall কখন কোনটা? ROC-AUC কী? Overfitting কীভাবে ধরবে?"),
    (6,2,"P2 · Classical ML","Supervised Learning II (Trees + Tuning)",
     "Decision trees (Gini, entropy, info gain), Random Forest (bagging), Gradient Boosting, XGBoost internals (regularized objective, split finding), LightGBM (leaf-wise), CatBoost (categorical), feature importance (gain, permutation, SHAP), GridSearch/RandomSearch/Optuna/Bayesian.",
     "StatQuest: Random Forest, XGBoost playlists | XGBoost docs | Optuna docs | SHAP docs",
     "Same dataset-এ Logistic vs RF vs XGBoost vs LightGBM — SHAP + permutation importance সহ ব্যাখ্যা। model_comparison.md লিখো।",
     "XGBoost কীভাবে কাজ করে? Bagging vs boosting? Feature importance কীভাবে calculate?"),
    (7,2,"P2 · Classical ML","Unsupervised Learning + PyTorch Fundamentals",
     "K-Means (Lloyd's, elbow, silhouette), DBSCAN, hierarchical, GMM, PCA (eigen + SVD), t-SNE, UMAP, autoencoder intro. PyTorch: tensors, CUDA (RTX 3050), autograd, computation graph, requires_grad, backward, optimizers, nn.Module intro.",
     "scikit-learn clustering + decomposition guides | PyTorch 60-min blitz | StatQuest PCA, t-SNE, UMAP",
     "K-Means + PCA visualization। Raw PyTorch-এ linear regression — manual gradient + autograd দুটোতেই।",
     "K-Means-এর limitation? PCA কীভাবে কাজ করে? t-SNE vs PCA?"),
    (8,2,"P2 · PyTorch","Neural Networks from Scratch (MLP, Backprop, Training Loop)",
     "Perceptron → MLP, activations (ReLU, GELU, SiLU, Sigmoid, Tanh), losses (MSE, CrossEntropy, BCE), forward/backward, weight init (Xavier, He), batch norm, dropout, LR, SGD/Adam/AdamW, training loop, early stopping, learning curves. PyTorch: Dataset, DataLoader, collate_fn, custom loop, lr_scheduler, checkpointing.",
     "Karpathy Neural Networks: Zero to Hero | PyTorch Neural Networks + Classifier tutorials | Goodfellow DL Ch.6-8",
     "MNIST-এ MLP — >98% test acc, loss curve, confusion matrix + scratch backprop notebook. Repo: mnist-mlp-from-scratch।",
     "Backprop হাতে derive? Batch norm কেন? Dropout কীভাবে regularize করে?"),
    (9,3,"P3 · DL (CV)","CNN Deep-Dive + Transfer Learning",
     "Convolution (kernel, stride, padding, dilation), pooling, receptive field, LeNet→AlexNet→VGG→ResNet→EfficientNet→ConvNeXt, residual connections, batch norm, transfer learning (feature extraction vs fine-tuning), augmentation (albumentations, torchvision), torchvision.models.",
     "CS231n lecture notes | torchvision docs | Albumentations docs",
     "Custom image dataset-এ pretrained ResNet-50 fine-tune — before/after accuracy compare। YAML config-driven train.py লিখো।",
     "ResNet skip connection কেন? Transfer learning কখন fail করে? Augmentation techniques?"),
    (10,3,"P3 · DL (CV)","Object Detection, Segmentation, Modern CV Pipeline",
     "Detection: YOLOv8/v11 internals, anchor-free (FCOS, CenterNet), one-stage vs two-stage (Faster R-CNN), mAP, NMS, IoU. Segmentation: U-Net, Mask R-CNN, SAM, panoptic. Tools: CVAT, Roboflow, Label Studio. Formats: COCO, YOLO, Pascal VOC.",
     "Ultralytics YOLO docs | Roboflow blog | SAM paper + demo | CS231n detection/segmentation lecture",
     "SignVision upgrade: detection + tracking (ByteTrack) বা segmentation যোগ। mAP before/after benchmark।",
     "One-stage vs two-stage? mAP কীভাবে calculate? NMS কী?"),
    (11,3,"P3 · DL (NLP)","NLP Foundations + Transformer from Scratch",
     "Tokenization (BPE, WordPiece, SentencePiece), embeddings (Word2Vec, GloVe, contextual), attention, self-attention, multi-head, positional encoding (sinusoidal + RoPE), layer norm, residual, encoder vs decoder, masked attention. 'Attention is All You Need' line-by-line.",
     "Jay Alammar Illustrated Transformer | Attention Is All You Need paper | Karpathy Let's build GPT | Harvard Annotated Transformer",
     "PyTorch-এ mini-GPT scratch থেকে — char-level, Shakespeare, training loop. Repo: gpt-from-scratch।",
     "Self-attention-এ Q,K,V কী? Multi-head কেন? Positional encoding কেন?"),
    (12,3,"P3 · DL (NLP)","HuggingFace Ecosystem + Fine-tuning Transformers",
     "transformers, datasets, tokenizers, accelerate, Trainer API, pipelines, model hub, model cards, fine-tuning BERT/DistilBERT/RoBERTa (classification, NER, QA, generation), metrics (GLUE, perplexity, F1).",
     "HuggingFace NLP course (official free) | transformers docs | datasets docs",
     "DistilBERT fine-tune text classification → HF Hub push with model card + inference API wrapper।",
     "BERT vs GPT? Fine-tune vs feature extraction? Subword tokenization কেন?"),
    (13,3,"P3 · DL Review","Phase 3 Review + Model Selection Framework",
     "Model selection: CNN vs Transformer vs classical ML vs LLM. Error analysis, ablation studies, benchmark reading (Papers with Code), compute budget, latency vs accuracy, model cards, responsible AI basics.",
     "Papers with Code leaderboards | Goodfellow DL Ch.11 | Your weeks 9-12 notebooks",
     "Decision framework doc: 'which model family for which problem' — flowchart + reasoning সহ।",
     "নতুন problem-এ কোন model? Tradeoffs? Model evaluate কীভাবে?"),
    (14,4,"P4 · MLOps","Experiment Tracking + Reproducibility",
     "MLflow (tracking, projects, models, registry), Weights & Biases (sweeps, artifacts), DVC data/model versioning, Git LFS, reproducibility (seed, env pinning, containerization), Hydra/OmegaConf config.",
     "MLflow docs | W&B docs (free) | DVC start guide | Hydra docs",
     "Training script-এ MLflow যোগ — ৩+ run compare dashboard। DVC দিয়ে dataset version।",
     "Reproducibility কীভাবে নিশ্চিত? Experiment tracking কেন?"),
    (15,4,"P4 · MLOps","Model Serving (FastAPI + Docker + ONNX + Batching)",
     "FastAPI serving, Pydantic validation, async inference, dynamic batching, ONNX export + onnxruntime, TorchScript, TensorRT basics, gRPC vs REST, health checks, locust/k6 load test, rate limiting, autoscaling.",
     "FastAPI docs | ONNX Runtime docs | Designing ML Systems Ch.7 | Locust docs",
     "Trained model Dockerized FastAPI-তে serve — health check, batching, ONNX conversion, locust load test।",
     "Model serve-এ কী consider? ONNX কেন? Batching latency কীভাবে কমায়?"),
    (16,4,"P4 · MLOps","Data Pipelines, Feature Stores, Orchestration",
     "DVC pipelines, Prefect/Airflow DAG, feature stores (Feast concept), data validation (Great Expectations, Pandera), scheduled retraining, incremental training, drift triggers, ETL for ML.",
     "Prefect docs | Airflow tutorial | Feast docs | Great Expectations docs",
     "Prefect DAG: new data → validate → retrain → evaluate → register (MLflow)।",
     "Retraining কীভাবে automate? Feature store কী? Data validation কেন?"),
    (17,4,"P4 · MLOps","Monitoring, Drift Detection, Observability",
     "Data drift (KS test, PSI, JS), concept drift, model drift, Evidently AI, Prometheus exporters for ML, Grafana dashboards, prediction logging, tracing, alerting, shadow deployment, canary, production A/B.",
     "Evidently AI docs | Prometheus Python client | Grafana docs | Designing ML Systems Ch.8",
     "Model latency + prediction distribution Prometheus exporter → Grafana dashboard। TurfSync setup extend।",
     "Drift কীভাবে ধরবে? Silent failure? Monitoring-এ কী metrics?"),
    (18,5,"P5 · LLM/GenAI","LLM Fundamentals + Advanced Prompt Engineering",
     "LLM training (pretrain → SFT → RLHF/DPO), tokenization, context window, temperature/top-p, prompt patterns (zero-shot, few-shot, CoT, ReAct, self-consistency), structured output (JSON mode, function calling, tool use), constrained decoding (grammar, outlines), eval (LLM-as-judge, human), cost/token accounting.",
     "Anthropic prompt engineering docs | promptingguide.ai | OpenAI cookbook | ReAct + CoT papers",
     "Real use case-এ ৫ prompt template — A/B test quality/consistency। Pydantic + JSON schema structured extractor।",
     "CoT কেন কাজ করে? Structured output কীভাবে নিশ্চিত? Prompt injection কী?"),
    (19,5,"P5 · LLM/GenAI","Embeddings + Vector Databases (Internals)",
     "Embedding models (OpenAI, Cohere, sentence-transformers, BGE, E5), similarity (cosine, dot, euclidean), ANN: HNSW, IVF, PQ, ScaNN. Vector DB: Qdrant, Pinecone, Weaviate, Milvus, pgvector, Chroma. Metadata filtering, hybrid search (BM25 + vector), index tuning (M, ef_construction, nlist).",
     "Qdrant docs + blog | Supabase pgvector guide | Pinecone learning center | HNSW paper",
     "pgvector + Qdrant দুটোতেই same document set-এ semantic search — latency/setup compare। embeddings_benchmark.md।",
     "HNSW কীভাবে কাজ করে? Cosine vs dot? pgvector vs Pinecone কখন?"),
    (20,5,"P5 · LLM/GenAI","RAG (Basic → Advanced)",
     "Chunking (fixed, semantic, recursive, parent-child), retrieval, reranking (cross-encoder, Cohere rerank, bge-reranker), query rewriting (HyDE, multi-query), hybrid search, context compression, citation, evaluation (RAGAS: faithfulness, answer relevancy, context precision/recall), LangChain vs LlamaIndex vs hand-rolled, agentic RAG.",
     "LangChain RAG tutorial | LlamaIndex docs | RAGAS docs | RAG paper (Lewis et al.)",
     "নিজের resume/papers/projects-এর উপর RAG chatbot — FastAPI + Docker deploy, RAGAS eval। Repo: rag-chatbot।",
     "Basic RAG failure modes? Reranking কেন? RAGAS কী measure করে?"),
    (21,5,"P5 · LLM/GenAI","LLM Fine-tuning (LoRA/QLoRA/DPO)",
     "PEFT: LoRA, QLoRA (4-bit), adapter layers, prefix/prompt tuning. SFT, DPO/ORPO/RLHF concept. Chat templates, RTX 3050 constraints (1-3B QLoRA), eval, catastrophic forgetting, LoRA merging, quantization (GPTQ, AWQ, GGUF).",
     "HF PEFT docs | HF TRL docs | LoRA + QLoRA papers | Unsloth docs",
     "Small open model (Phi-3-mini/Llama-3.2-1B/Qwen2.5-1.5B) QLoRA fine-tune narrow task। base vs fine-tuned compare।",
     "LoRA কীভাবে কাজ করে? RAG vs fine-tune? QLoRA কী সেভ করে?"),
    (22,5,"P5 · LLM/GenAI","LLM Agents, Tool Use, Multi-Agent Systems",
     "Function calling, tool use, ReAct, planning (Plan-and-Execute), reflection, memory (short/long-term), multi-agent (AutoGen, CrewAI, LangGraph), agent evaluation, sandboxing, tool safety, MCP (Model Context Protocol), computer use.",
     "LangGraph docs | Anthropic Building Effective Agents blog | AutoGen + CrewAI docs | MCP spec",
     "Multi-tool agent (data analyst: SQL query + chart + summary) LangGraph state machine দিয়ে।",
     "Agent কীভাবে plan করে? Tool use-এ error handling? Multi-agent কখন দরকার?"),
    (23,5,"P5 · LLM/GenAI","LLM Serving, Optimization, Observability",
     "vLLM (PagedAttention), TGI, llama.cpp, Ollama, Triton. Quantization (GPTQ, AWQ, GGUF), speculative decoding, KV cache, continuous batching, prompt caching. Observability: LangSmith, Langfuse, Phoenix (Arize), tracing, token cost, hallucination detection, guardrails (NeMo, Guardrails AI).",
     "vLLM docs + PagedAttention paper | Langfuse docs | Ollama docs | NeMo Guardrails docs",
     "Open model vLLM-এ serve — throughput/latency benchmark। Langfuse tracing যোগ।",
     "vLLM কেন দ্রুত? Quantization-এ accuracy loss? Hallucination কীভাবে ধরবে?"),
    (24,6,"P6 · Capstone","ML System Design + Interview Prep",
     "ML system design framework (problem → data → model → serving → monitoring). Case studies: recommendation, fraud, search ranking, RAG, real-time inference. Tradeoffs: latency vs accuracy, cost vs quality, batch vs online. A/B testing, MLOps maturity. Behavioral: STAR, project deep-dives.",
     "Designing ML Systems (Chip Huyen) | ML System Design Interview (Aminian) | Exponent YouTube",
     "৩টা ML system design mock (recommendation, fraud, RAG) — প্রতিটা 2-page doc + diagram।",
     "Interview-focused week — পুরো সপ্তাহ practice।"),
    (25,6,"P6 · Capstone","Capstone Project 1 — Production CV System (build)",
     "Design decisions: problem framing, dataset selection (reuse SignVision or new), model architecture choice (YOLO/ResNet), evaluation protocol (mAP, latency), serving plan (FastAPI + Docker), monitoring plan (Prometheus/Grafana + Evidently drift), CI/CD, reproducibility (DVC + MLflow).",
     "Reuse weeks 9-10 (CNN, detection) + 15 (serving) + 17 (monitoring). Reference: Ultralytics docs, FastAPI docs, Evidently AI docs.",
     "Start Project 1: build training pipeline → model training → FastAPI serving → Docker Compose → Prometheus metrics → Grafana dashboard. Push initial repo with README + architecture diagram.",
     "Project-এ কোন tradeoff নিয়েছ? Production-এ কীভাবে deploy করবে? Monitoring কীভাবে করবে?"),
    (26,6,"P6 · Capstone","Capstone Project 2 — RAG/LLM Production Tool + Portfolio Polish",
     "RAG system: hybrid search (BM25 + vector), reranking, chunking, RAGAS evaluation. Backend: FastAPI/NestJS, vector DB (pgvector/Qdrant), LLM API, auth, rate limiting, Docker, Langfuse tracing. Portfolio: resume/LinkedIn/GitHub update, months 7-12 roadmap.",
     "Reuse weeks 18-23 (LLM, RAG, agents, serving) + weeks 14-17 (MLOps). Reference: LangChain RAG tutorial, RAGAS docs, Langfuse docs.",
     "GitHub-এ production RAG repo — README + demo + design tradeoffs write-up. Resume + LinkedIn + GitHub polish. Months 7-12 plan doc (advanced topics: distributed training, multi-modal, RLHF, quantization).",
     "Fine-tune vs RAG — কী বেছেছ এবং কেন? Cost কীভাবে control করেছ? Hallucination কীভাবে ধরবে?"),
]

MILESTONES = [
    ("Month 1","Can clean/explore a dataset and explain backprop with chain rule on paper.","Could I explain gradient descent to a junior dev in 5 minutes?"),
    ("Month 2","Trained + evaluated 3 classical ML models and a from-scratch PyTorch MLP on MNIST (>98%).","Do I know when to pick XGBoost over a neural net?"),
    ("Month 3","Fine-tuned a CNN (CV) and a small Transformer (NLP); wrote a model-choice decision doc.","Can I justify CNN vs Transformer vs classical ML for a new problem?"),
    ("Month 4","A trained model is served via Dockerized FastAPI with logging + a Grafana dashboard.","Could this survive 100 concurrent requests? Would I know if it silently broke?"),
    ("Month 5","Shipped a working RAG chatbot and one LoRA fine-tune experiment.","Do I know when to fine-tune vs RAG vs prompting for a business problem?"),
    ("Month 6","2 portfolio projects live on GitHub with docs + demos; resume/LinkedIn updated.","Would a senior AI engineer approve this code in a review?"),
]

PROJECTS = [
    ("Project 1: Production CV Pipeline","PyTorch, YOLO/ResNet, FastAPI, Docker, Prometheus/Grafana, DVC, MLflow","25","End-to-end CV system: data → train → serve → monitor, on GitHub with README + architecture diagram + demo GIF + monitoring screenshots"),
    ("Project 2: RAG/LLM Backend Tool","NestJS/FastAPI, LLM API, Vector DB (pgvector/Qdrant), Docker, Langfuse, RAGAS","26","RAG-based tool solving a real workflow problem, deployed, documented, with evaluation report + demo"),
]

RESOURCES = [
    ("Python/Math","Fluent Python (2nd ed) — Luciano Ramalho","Book","Paid"),
    ("Python/Math","NumPy Beginners Guide","numpy.org/doc/stable/user/absolute_beginners.html","Free"),
    ("Python/Math","Pandas Getting Started","pandas.pydata.org/docs/getting_started/intro_tutorials","Free"),
    ("Python/Math","Kaggle Learn","kaggle.com/learn","Free"),
    ("Python/Math","3Blue1Brown — Essence of Linear Algebra","YouTube","Free"),
    ("Python/Math","3Blue1Brown — Essence of Calculus","YouTube","Free"),
    ("Python/Math","StatQuest with Josh Starmer","YouTube","Free"),
    ("Python/Math","Probabilistic ML: An Introduction — Kevin Murphy","probml.github.io/pml-book","Free PDF"),
    ("Classical ML","Andrew Ng — Machine Learning Specialization","coursera.org","Free audit"),
    ("Classical ML","scikit-learn User Guide","scikit-learn.org/stable/user_guide.html","Free"),
    ("Classical ML","XGBoost Docs","xgboost.readthedocs.io","Free"),
    ("Classical ML","Optuna Docs","optuna.readthedocs.io","Free"),
    ("Classical ML","SHAP Docs","shap.readthedocs.io","Free"),
    ("Deep Learning","PyTorch 60-Minute Blitz","pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html","Free"),
    ("Deep Learning","Karpathy — Neural Networks: Zero to Hero","YouTube","Free"),
    ("Deep Learning","Karpathy — Let's build GPT from scratch","YouTube","Free"),
    ("Deep Learning","Deep Learning — Goodfellow, Bengio, Courville","deeplearningbook.org","Free online"),
    ("DL (CV)","CS231n Stanford","cs231n.github.io","Free"),
    ("DL (CV)","Ultralytics YOLO Docs","docs.ultralytics.com","Free"),
    ("DL (CV)","Meta Segment Anything (SAM)","segment-anything.com","Free"),
    ("DL (CV)","Albumentations Docs","albumentations.ai/docs","Free"),
    ("DL (NLP)","The Illustrated Transformer — Jay Alammar","jalammar.github.io/illustrated-transformer","Free"),
    ("DL (NLP)","Attention Is All You Need (paper)","arxiv.org/abs/1706.03762","Free"),
    ("DL (NLP)","HuggingFace NLP Course","huggingface.co/learn/nlp-course","Free"),
    ("MLOps","MLflow Docs","mlflow.org/docs/latest","Free"),
    ("MLOps","Weights & Biases","wandb.ai/site","Free tier"),
    ("MLOps","DVC (Data Version Control)","dvc.org/doc/start","Free"),
    ("MLOps","Prefect Quickstart","docs.prefect.io","Free tier"),
    ("MLOps","Evidently AI","docs.evidentlyai.com","Free"),
    ("MLOps","ONNX Runtime Docs","onnxruntime.ai/docs","Free"),
    ("MLOps","Locust (load testing)","locust.io","Free"),
    ("MLOps","Designing Machine Learning Systems — Chip Huyen","O'Reilly","Paid"),
    ("LLM/GenAI","Anthropic Prompt Engineering Docs","docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview","Free"),
    ("LLM/GenAI","Prompt Engineering Guide","promptingguide.ai","Free"),
    ("LLM/GenAI","Qdrant Docs","qdrant.tech/documentation","Free tier"),
    ("LLM/GenAI","Supabase pgvector Guide","supabase.com/docs/guides/ai","Free tier"),
    ("LLM/GenAI","LangChain RAG Tutorial","python.langchain.com/docs/tutorials/rag","Free"),
    ("LLM/GenAI","LlamaIndex Docs","llamaindex.ai","Free"),
    ("LLM/GenAI","RAGAS (RAG eval)","docs.ragas.io","Free"),
    ("LLM/GenAI","HuggingFace PEFT (LoRA/QLoRA)","huggingface.co/docs/peft","Free"),
    ("LLM/GenAI","HF TRL (SFT/DPO)","huggingface.co/docs/trl","Free"),
    ("LLM/GenAI","Unsloth (fast LoRA)","github.com/unslothai/unsloth","Free"),
    ("LLM/GenAI","LangGraph Docs","langchain-ai.github.io/langgraph","Free"),
    ("LLM/GenAI","Anthropic — Building Effective Agents","anthropic.com/engineering","Free"),
    ("LLM/GenAI","vLLM Docs","docs.vllm.ai","Free"),
    ("LLM/GenAI","Langfuse (LLM observability)","langfuse.com/docs","Free tier"),
    ("LLM/GenAI","NeMo Guardrails","github.com/NVIDIA/NeMo-Guardrails","Free"),
    ("Reference","Papers with Code","paperswithcode.com","Free"),
    ("Reference","ML System Design Interview — Aminian & Xu","Book","Paid"),
]

wb = Workbook()

# ================== DASHBOARD ==================
ws = wb.active
ws.title = "Dashboard"
ws.column_dimensions["A"].width = 4
ws.column_dimensions["B"].width = 42
ws.column_dimensions["C"].width = 22

ws["B2"] = "AI Engineer Transition — 6 Month Deep-Dive Tracker"
ws["B2"].font = TITLE_FONT
ws["B3"] = "Awolad Hossain — Backend Engineer → AI Engineer (DATAZLY Technologies)"
ws["B3"].font = SUBTITLE_FONT

ws["B5"] = "Metric"; ws["B5"].font = HEADER_FONT; ws["B5"].fill = HEADER_FILL
ws["C5"] = "Value"; ws["C5"].font = HEADER_FONT; ws["C5"].fill = HEADER_FILL

metrics = [
    ("Program start date","=TODAY()"),
    ("Program length (weeks)","=COUNTA('Deep Dive Syllabus'!A5:A30)"),
    ("Target hours / week",10),
    ("Total target hours (26 wks)","=SUM('Deep Dive Syllabus'!I5:I30)"),
    ("Hours completed so far","=SUM('Deep Dive Syllabus'!J5:J30)"),
    ("% of program complete","=IFERROR(J10/I9,0)"),
    ("Weeks marked Done",'=COUNTIF(\'Deep Dive Syllabus\'!K5:K30,"Done")'),
    ("Weeks In Progress",'=COUNTIF(\'Deep Dive Syllabus\'!K5:K30,"In Progress")'),
    ("Weeks Not Started",'=COUNTIF(\'Deep Dive Syllabus\'!K5:K30,"Not Started")'),
]
for i,(k,v) in enumerate(metrics, start=6):
    ws[f"B{i}"] = k
    ws[f"C{i}"] = v
    ws[f"C{i}"].alignment = CENTER
ws["C11"].number_format = "0.0%"

ws["B17"] = "How to use"; ws["B17"].font = SUBHEADER_FONT; ws["B17"].fill = SUBHEADER_FILL
how_to = [
    "1. 'Deep Dive Syllabus' — 26 weeks: topics, resources, deliverables, interview angles.",
    "2. Every week: fill 'Hrs Done', set 'Status', add notes.",
    "3. Dashboard updates automatically.",
    "4. 'Monthly Milestones' — check progress each month.",
    "5. 'Projects' — 2 capstone portfolio projects.",
    "6. 'Resource Library' — every link in one place.",
    "7. Status dropdown: Not Started / In Progress / Done (colors update automatically).",
    "8. Use AutoFilter on row 4 to filter by Month or Phase.",
]
for i,line in enumerate(how_to, start=18):
    ws[f"B{i}"] = line

# ================== DEEP DIVE SYLLABUS ==================
ws2 = wb.create_sheet("Deep Dive Syllabus")
headers = ["Wk","Month","Phase","Focus Topic","Deep-Dive Topics","Resources","Hands-on Deliverable","Interview Angle","Target Hrs","Hrs Done","Status","Notes"]
ws2["A1"] = "26-Week Deep-Dive Plan — 10 hrs/week — Backend Engineer to AI Engineer"
ws2["A1"].font = TITLE_FONT
ws2["A2"] = "P1 Python+Math | P2 Classical ML+PyTorch | P3 DL (CV+NLP) | P4 MLOps | P5 LLM/GenAI | P6 Capstone"
ws2["A2"].font = SUBTITLE_FONT

for col,h in enumerate(headers, start=1):
    c = ws2.cell(row=4, column=col, value=h)
    c.font = HEADER_FONT; c.fill = HEADER_FILL; c.alignment = CENTER; c.border = BORDER

for i,row in enumerate(SYLLABUS):
    r = 5+i
    week,month,phase,focus,deep,res,deliv,angle = row
    ws2.cell(row=r,column=1,value=week).alignment = CENTER
    ws2.cell(row=r,column=2,value=month).alignment = CENTER
    ws2.cell(row=r,column=3,value=phase)
    ws2.cell(row=r,column=4,value=focus)
    ws2.cell(row=r,column=5,value=deep)
    ws2.cell(row=r,column=6,value=res)
    ws2.cell(row=r,column=7,value=deliv)
    ws2.cell(row=r,column=8,value=angle)
    ws2.cell(row=r,column=9,value=10).alignment = CENTER
    ws2.cell(row=r,column=10,value=0).alignment = CENTER
    ws2.cell(row=r,column=11,value="Not Started").alignment = CENTER
    ws2.cell(row=r,column=12,value="")
    for col in range(1,13):
        cell = ws2.cell(row=r,column=col)
        cell.border = BORDER
        if col in (4,5,6,7,8):
            cell.alignment = WRAP

widths = [6,7,18,28,60,40,45,45,10,10,14,20]
for i,w in enumerate(widths, start=1):
    ws2.column_dimensions[chr(64+i)].width = w

dv = DataValidation(type="list", formula1='"Not Started,In Progress,Done"', allow_blank=True)
ws2.add_data_validation(dv)
dv.add("K5:K30")

# --- Conditional formatting for Status column ---
ws2.conditional_formatting.add("K5:K30",
    CellIsRule(operator="equal", formula=['"Done"'], fill=DONE_FILL, font=DONE_FONT))
ws2.conditional_formatting.add("K5:K30",
    CellIsRule(operator="equal", formula=['"In Progress"'], fill=PROGRESS_FILL, font=PROGRESS_FONT))
ws2.conditional_formatting.add("K5:K30",
    CellIsRule(operator="equal", formula=['"Not Started"'], fill=NOT_STARTED_FILL, font=NOT_STARTED_FONT))

# --- AutoFilter ---
ws2.auto_filter.ref = "A4:L30"
ws2.freeze_panes = "A5"

# ================== MONTHLY MILESTONES ==================
ws3 = wb.create_sheet("Monthly Milestones")
ws3["A1"] = "Monthly Milestones & Self-Check"
ws3["A1"].font = TITLE_FONT
heads = ["Month","Milestone (must hit to stay on track)","Self-check question","Status","Notes"]
for col,h in enumerate(heads, start=1):
    c = ws3.cell(row=3, column=col, value=h)
    c.font = HEADER_FONT; c.fill = HEADER_FILL; c.alignment = CENTER; c.border = BORDER
for i,(m,ms,q) in enumerate(MILESTONES, start=4):
    ws3.cell(row=i,column=1,value=m)
    ws3.cell(row=i,column=2,value=ms)
    ws3.cell(row=i,column=3,value=q)
    ws3.cell(row=i,column=4,value="Not Started")
    ws3.cell(row=i,column=5,value="")
    for col in range(1,6):
        c = ws3.cell(row=i,column=col); c.border = BORDER
        if col in (2,3): c.alignment = WRAP
dv3 = DataValidation(type="list", formula1='"Not Started,In Progress,Done"', allow_blank=True)
ws3.add_data_validation(dv3); dv3.add("D4:D9")

# Conditional formatting for Milestones status
ws3.conditional_formatting.add("D4:D9",
    CellIsRule(operator="equal", formula=['"Done"'], fill=DONE_FILL, font=DONE_FONT))
ws3.conditional_formatting.add("D4:D9",
    CellIsRule(operator="equal", formula=['"In Progress"'], fill=PROGRESS_FILL, font=PROGRESS_FONT))
ws3.conditional_formatting.add("D4:D9",
    CellIsRule(operator="equal", formula=['"Not Started"'], fill=NOT_STARTED_FILL, font=NOT_STARTED_FONT))

for i,w in enumerate([10,60,55,14,25], start=1):
    ws3.column_dimensions[chr(64+i)].width = w

# ================== PROJECTS ==================
ws4 = wb.create_sheet("Projects")
ws4["A1"] = "Portfolio Projects"
ws4["A1"].font = TITLE_FONT
heads = ["Project","Stack","Weeks","Deliverable","Status","GitHub Link"]
for col,h in enumerate(heads, start=1):
    c = ws4.cell(row=3, column=col, value=h)
    c.font = HEADER_FONT; c.fill = HEADER_FILL; c.alignment = CENTER; c.border = BORDER
for i,(p,s,w,d) in enumerate(PROJECTS, start=4):
    ws4.cell(row=i,column=1,value=p)
    ws4.cell(row=i,column=2,value=s)
    ws4.cell(row=i,column=3,value=w)
    ws4.cell(row=i,column=4,value=d)
    ws4.cell(row=i,column=5,value="Not Started")
    ws4.cell(row=i,column=6,value="")
    for col in range(1,7):
        c = ws4.cell(row=i,column=col); c.border = BORDER
        if col in (2,4): c.alignment = WRAP
dv4 = DataValidation(type="list", formula1='"Not Started,In Progress,Done"', allow_blank=True)
ws4.add_data_validation(dv4); dv4.add("E4:E5")

ws4.conditional_formatting.add("E4:E5",
    CellIsRule(operator="equal", formula=['"Done"'], fill=DONE_FILL, font=DONE_FONT))
ws4.conditional_formatting.add("E4:E5",
    CellIsRule(operator="equal", formula=['"In Progress"'], fill=PROGRESS_FILL, font=PROGRESS_FONT))
ws4.conditional_formatting.add("E4:E5",
    CellIsRule(operator="equal", formula=['"Not Started"'], fill=NOT_STARTED_FILL, font=NOT_STARTED_FONT))

for i,w in enumerate([32,45,10,55,14,35], start=1):
    ws4.column_dimensions[chr(64+i)].width = w

# ================== RESOURCE LIBRARY ==================
ws5 = wb.create_sheet("Resource Library")
ws5["A1"] = "Resource Library (every link in one place)"
ws5["A1"].font = TITLE_FONT
heads = ["Category","Resource","Link","Cost"]
for col,h in enumerate(heads, start=1):
    c = ws5.cell(row=3, column=col, value=h)
    c.font = HEADER_FONT; c.fill = HEADER_FILL; c.alignment = CENTER; c.border = BORDER
for i,(cat,res,link,cost) in enumerate(RESOURCES, start=4):
    ws5.cell(row=i,column=1,value=cat)
    ws5.cell(row=i,column=2,value=res)
    ws5.cell(row=i,column=3,value=link)
    ws5.cell(row=i,column=4,value=cost)
    for col in range(1,5):
        ws5.cell(row=i,column=col).border = BORDER
for i,w in enumerate([16,55,60,14], start=1):
    ws5.column_dimensions[chr(64+i)].width = w

ws5.auto_filter.ref = f"A3:D{3+len(RESOURCES)}"

# ================== SAVE ==================
out = "AI_Engineer_6Month_DeepDive.xlsx"
wb.save(out)
print(f"✅ Created: {out}")
print(f"   Sheets: Dashboard, Deep Dive Syllabus, Monthly Milestones, Projects, Resource Library")
print(f"   Syllabus rows: {len(SYLLABUS)}")
print(f"   Milestones: {len(MILESTONES)}")
print(f"   Projects: {len(PROJECTS)}")
print(f"   Resources: {len(RESOURCES)}")
