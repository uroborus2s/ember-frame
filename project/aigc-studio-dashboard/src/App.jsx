import {
  Archive,
  Bot,
  ChevronRight,
  CircleDot,
  Clapperboard,
  Download,
  Film,
  FolderGit2,
  GitBranch,
  ListChecks,
  MonitorPlay,
  Play,
  Plus,
  Radio,
  Search,
  Send,
  Settings2,
  ShieldCheck,
  Sparkles,
  Wand2,
} from "lucide-react";
import { useCallback, useMemo, useState } from "react";
import {
  Background,
  Controls,
  Handle,
  MarkerType,
  MiniMap,
  Position,
  ReactFlow,
  addEdge,
  useEdgesState,
  useNodesState,
} from "@xyflow/react";

import {
  automationSteps,
  gameEvents,
  initialEdges,
  initialNodes,
  localModelRoutes,
  logs,
  queue,
  stageTabs,
  studioRooms,
  vault,
  versions,
} from "./data";
import Art25DScene from "./Art25DScene";

function statusLabel(status) {
  return {
    active: "进行中",
    locked: "已锁定",
    ready: "可交接",
    queued: "排队中",
    risk: "高风险",
    review: "复核中",
    waiting: "等待中",
  }[status] || status;
}

function StudioNode({ data, selected }) {
  return (
    <article
      className={`studio-node ${selected ? "is-selected" : ""} ${data.dimmed ? "is-dimmed" : ""}`}
      style={{ "--node-accent": data.accent }}
    >
      <Handle type="target" position={Position.Left} />
      <div className="node-topline">
        <span className={`node-status status-${data.status}`}>{statusLabel(data.status)}</span>
        <span>{data.owner}</span>
      </div>
      <h3>{data.title}</h3>
      <p>{data.subtitle}</p>
      <div className="node-progress" aria-label={`${data.title} progress`}>
        <i style={{ width: `${data.progress}%` }} />
      </div>
      <div className="node-tags">
        {data.badges.map((badge) => (
          <span key={badge}>{badge}</span>
        ))}
      </div>
      <Handle type="source" position={Position.Right} />
    </article>
  );
}

const nodeTypes = { studio: StudioNode };

function IconButton({ icon: Icon, label, active = false, onClick }) {
  return (
    <button className={`icon-button ${active ? "is-active" : ""}`} onClick={onClick} type="button">
      <Icon size={16} />
      <span>{label}</span>
    </button>
  );
}

function StudioBuilding() {
  return (
    <section className="building-panel">
      <div className="panel-title">
        <span><Clapperboard size={16} /> 制片楼实时运作</span>
        <small>v013 干净透明窗 + 无晃车流 GIF</small>
      </div>

      <Art25DScene />

      <div className="game-event-strip">
        {gameEvents.map((event) => (
          <article key={event.title}>
            <span>{event.from} &gt; {event.to}</span>
            <strong>{event.title}</strong>
            <b>{event.state}</b>
          </article>
        ))}
      </div>
    </section>
  );
}

function RoomRoster({ activeRoomId, onSelectRoom }) {
  return (
    <section className="room-roster">
      {studioRooms.map((room) => (
        <button
          className={activeRoomId === room.id ? "is-active" : ""}
          key={room.id}
          onClick={() => onSelectRoom(room)}
          type="button"
        >
          <span className="nav-dot" style={{ "--tone": room.accent }} />
          <div>
            <strong>{room.name}</strong>
            <small>{room.role}</small>
          </div>
          <b>{room.state}</b>
        </button>
      ))}
    </section>
  );
}

function CommandCenter({ command, onCommandChange, onStart, automationRunning }) {
  return (
    <section className="command-center">
      <div className="panel-title">
        <span><Sparkles size={16} /> 一句话自动制片</span>
        <small>{automationRunning ? "自动推进中" : "等待指令"}</small>
      </div>

      <form className="command-box" onSubmit={onStart}>
        <textarea
          onChange={(event) => onCommandChange(event.target.value)}
          placeholder="例如：把 G-P 边墙段落自动做成 45 秒预告片，保持角色一致，优先用本地 Wan。"
          value={command}
        />
        <button type="submit">
          <Send size={16} />
          <span>启动自动制作</span>
        </button>
      </form>

      <div className="automation-flow">
        {automationSteps.map((step) => (
          <article className={`step-card step-${step.state}`} key={step.room}>
            <b>{step.room}</b>
            <span>{step.task}</span>
          </article>
        ))}
      </div>
    </section>
  );
}

function CharacterPipelinePanel() {
  return (
    <section className="character-pipeline">
      <div className="panel-title">
        <span><Bot size={16} /> 正式美术预览</span>
        <small>母图拆包 + 角色切帧</small>
      </div>
      <div className="pipeline-steps">
        <article>
          <strong>空间</strong>
          <span>办公室主视觉已进入页面，后续继续拆精确前景层。</span>
        </article>
        <article>
          <strong>人物</strong>
          <span>男女中国职场卡通动作表已切成四方向透明 sprite。</span>
        </article>
        <article>
          <strong>动作</strong>
          <span>当前改为手动办公室移动，固定工位人员持续打字办公。</span>
        </article>
      </div>
    </section>
  );
}

function LocalModelPanel({ selectedNode }) {
  const [endpoint, setEndpoint] = useState(localModelRoutes[0].endpoint);
  const [status, setStatus] = useState("未检测");

  const checkEndpoint = useCallback(async () => {
    setStatus("检测中");
    try {
      const base = endpoint.replace(/\/$/, "");
      const response = await fetch(`${base}/system_stats`, { method: "GET" });
      setStatus(response.ok ? "ComfyUI 可连接" : `HTTP ${response.status}`);
    } catch {
      setStatus("未连接或被 CORS 拦截");
    }
  }, [endpoint]);

  return (
    <section className="local-model-panel">
      <div className="panel-title">
        <span><Radio size={16} /> 本地模型路由</span>
        <small>{status}</small>
      </div>

      <div className="endpoint-row">
        <input value={endpoint} onChange={(event) => setEndpoint(event.target.value)} />
        <button onClick={checkEndpoint} type="button">检测</button>
      </div>

      <div className="route-list">
        {localModelRoutes.map((route) => (
          <article key={route.id}>
            <strong>{route.name}</strong>
            <span>{route.method}</span>
            <small>{route.use}</small>
          </article>
        ))}
      </div>

      <div className="payload-card">
        <b>当前节点下发包</b>
        <code>
          {JSON.stringify(
            {
              node: selectedNode?.id,
              workflow: selectedNode?.data?.title,
              endpoint,
              mode: "local-first",
            },
            null,
            2
          )}
        </code>
      </div>
    </section>
  );
}

function Inspector({ selectedNode, onQueueRetake }) {
  const data = selectedNode?.data;

  return (
    <aside className="inspector role-inspector">
      <div className="panel-title">
        <span><Settings2 size={16} /> 岗位节点</span>
        <button type="button"><Archive size={15} /></button>
      </div>

      {data ? (
        <>
          <section className="inspector-hero" style={{ "--node-accent": data.accent }}>
            <div>
              <span className={`node-status status-${data.status}`}>{statusLabel(data.status)}</span>
              <h2>{data.title}</h2>
              <p>{data.subtitle}</p>
            </div>
            <strong>{data.progress}%</strong>
          </section>

          <section className="inspector-section">
            <h3>岗位闸门</h3>
            <div className="check-list">
              {data.checklist.map((item) => (
                <label key={item}>
                  <input type="checkbox" defaultChecked={data.progress > 55} />
                  <span>{item}</span>
                </label>
              ))}
            </div>
          </section>

          <section className="inspector-section">
            <h3>绑定资料</h3>
            <div className="vault-list compact">
              {vault.slice(0, 4).map((item) => (
                <button key={item} type="button">
                  <FolderGit2 size={14} />
                  <span>{item}</span>
                </button>
              ))}
            </div>
          </section>

          <div className="inspector-actions">
            <IconButton icon={Play} label="运行节点" />
            <IconButton icon={Plus} label="加入返修" onClick={onQueueRetake} />
          </div>
        </>
      ) : (
        <div className="empty-state">
          <CircleDot size={22} />
          <span>未选择节点</span>
        </div>
      )}
    </aside>
  );
}

function QueuePanel() {
  return (
    <section className="queue-panel">
      <div className="panel-title">
        <span><ListChecks size={16} /> 自动队列</span>
        <button type="button"><ChevronRight size={16} /></button>
      </div>
      <div className="queue-list">
        {queue.map((item) => (
          <article key={item.id}>
            <div>
              <strong>{item.id}</strong>
              <span>{item.title}</span>
            </div>
            <small>{item.owner}</small>
            <b className={`risk risk-${item.risk}`}>{item.risk}</b>
            <em>{item.state}</em>
          </article>
        ))}
      </div>
    </section>
  );
}

function VersionRail() {
  return (
    <section className="version-rail">
      <div className="panel-title">
        <span><Film size={16} /> 镜头版本</span>
        <button type="button"><Download size={15} /></button>
      </div>
      <div className="version-grid">
        {versions.map((item) => (
          <article key={item.id}>
            <header>
              <strong>{item.id}</strong>
              <span>{item.version}</span>
            </header>
            <div className="score-line"><i style={{ width: `${item.score}%` }} /></div>
            <footer>
              <span>{item.state}</span>
              <b>{item.score}</b>
            </footer>
          </article>
        ))}
      </div>
    </section>
  );
}

export default function App() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(
    initialEdges.map((edge) => ({
      ...edge,
      markerEnd: { type: MarkerType.ArrowClosed, color: "#6edfd4" },
      style: { stroke: "#6edfd4", strokeWidth: 1.6 },
    }))
  );
  const [selectedId, setSelectedId] = useState("director-pack");
  const [activeRoomId, setActiveRoomId] = useState("director");
  const [activeTab, setActiveTab] = useState("总览");
  const [command, setCommand] = useState("把 G-P 边墙段落自动做成 45 秒预告片，优先调用本地 Wan，失败两轮再升级云模型。");
  const [automationRunning, setAutomationRunning] = useState(false);

  const selectedNode = useMemo(
    () => nodes.find((node) => node.id === selectedId),
    [nodes, selectedId]
  );

  const activeRoom = studioRooms.find((room) => room.id === activeRoomId) || studioRooms[0];

  const visibleNodes = useMemo(
    () =>
      nodes.map((node) => ({
        ...node,
        data: {
          ...node.data,
          dimmed: node.id !== activeRoom.nodeId && node.id !== selectedId,
        },
      })),
    [activeRoom.nodeId, nodes, selectedId]
  );

  const onConnect = useCallback(
    (params) =>
      setEdges((eds) =>
        addEdge(
          {
            ...params,
            animated: true,
            markerEnd: { type: MarkerType.ArrowClosed, color: "#6edfd4" },
            style: { stroke: "#6edfd4", strokeWidth: 1.6 },
          },
          eds
        )
      ),
    [setEdges]
  );

  const selectRoom = useCallback((room) => {
    setActiveRoomId(room.id);
    setSelectedId(room.nodeId);
  }, []);

  const startAutomation = useCallback((event) => {
    event.preventDefault();
    setAutomationRunning(true);
    setActiveRoomId("project");
    setSelectedId("source");
  }, []);

  const queueRetake = useCallback(() => {
    const source = selectedNode || nodes[0];
    const id = `retake-${Date.now()}`;
    const nextNode = {
      id,
      type: "studio",
      position: {
        x: source.position.x + 360,
        y: source.position.y + 190,
      },
      data: {
        department: "video",
        title: "自动返修任务",
        subtitle: `${source.data.title} / retake`,
        status: "queued",
        owner: "视频生成部",
        accent: "#77a7ff",
        progress: 12,
        eta: "新建",
        badges: ["retake", "local-first"],
        checklist: ["失败根因已写", "参考帧已绑定", "版本号已递增"],
      },
    };

    setNodes((nds) => nds.concat(nextNode));
    setEdges((eds) =>
      eds.concat({
        id: `e-${source.id}-${id}`,
        source: source.id,
        target: id,
        animated: true,
        markerEnd: { type: MarkerType.ArrowClosed, color: "#6edfd4" },
        style: { stroke: "#6edfd4", strokeWidth: 1.6 },
      })
    );
    setSelectedId(id);
    setActiveRoomId("video");
  }, [nodes, selectedNode, setEdges, setNodes]);

  return (
    <main className="app-shell">
      <header className="topbar">
        <section className="brand-block">
          <div className="brand-mark">羲</div>
          <div>
            <span>AIGC 智能制片楼</span>
            <h1>一句话自动完成的短剧生产系统</h1>
          </div>
        </section>

        <section className="top-metrics">
          <article><span>自动任务</span><strong>23</strong></article>
          <article><span>3D 场景</span><strong>1</strong></article>
          <article><span>本地模型</span><strong>3</strong></article>
          <article><span>导演复核</span><strong>2</strong></article>
        </section>

        <section className="top-actions">
          <IconButton icon={MonitorPlay} label="审片" />
          <IconButton icon={ShieldCheck} label="QC" />
          <IconButton icon={Download} label="导出" />
        </section>
      </header>

      <section className="studio-main">
        <StudioBuilding activeRoomId={activeRoomId} onSelectRoom={selectRoom} />
        <div className="control-column">
          <CommandCenter
            automationRunning={automationRunning}
            command={command}
            onCommandChange={setCommand}
            onStart={startAutomation}
          />
          <RoomRoster activeRoomId={activeRoomId} onSelectRoom={selectRoom} />
          <CharacterPipelinePanel />
          <LocalModelPanel selectedNode={selectedNode} />
        </div>
      </section>

      <section className="role-workspace">
        <div className="workspace-toolbar">
          <div>
            <span className="workspace-kicker">{activeRoom.name}</span>
            <h2>{activeRoom.role}</h2>
          </div>
          <div className="tab-strip">
            {stageTabs.map((tab) => (
              <button
                className={activeTab === tab ? "is-active" : ""}
                key={tab}
                onClick={() => setActiveTab(tab)}
                type="button"
              >
                {tab}
              </button>
            ))}
          </div>
          <div className="search-box">
            <Search size={15} />
            <input placeholder="搜索节点、资产、工作流" />
          </div>
          <div className="canvas-actions">
            <IconButton icon={GitBranch} label="连线" />
            <IconButton icon={Wand2} label="生成包" />
            <IconButton icon={Plus} label="返修" onClick={queueRetake} />
          </div>
        </div>

        <div className="role-grid">
          <section className="flow-shell role-flow">
            <ReactFlow
              colorMode="dark"
              edges={edges}
              fitView
              maxZoom={1.35}
              minZoom={0.25}
              nodes={visibleNodes}
              nodeTypes={nodeTypes}
              onConnect={onConnect}
              onEdgesChange={onEdgesChange}
              onNodeClick={(_, node) => setSelectedId(node.id)}
              onNodesChange={onNodesChange}
              proOptions={{ hideAttribution: true }}
            >
              <Background color="#2c4b4d" gap={28} size={1} />
              <Controls position="bottom-right" />
              <MiniMap
                maskColor="rgba(8, 16, 18, 0.66)"
                nodeBorderRadius={6}
                nodeColor={(item) => item.data?.accent || "#6edfd4"}
                position="bottom-left"
              />
            </ReactFlow>
          </section>

          <Inspector selectedNode={selectedNode} onQueueRetake={queueRetake} />
        </div>
      </section>

      <section className="bottom-dock">
        <QueuePanel />
        <VersionRail />
      </section>

      <footer className="event-log">
        <span><Bot size={15} /> 自动事件</span>
        {logs.map((log) => (
          <b key={log}>{log}</b>
        ))}
      </footer>
    </main>
  );
}
