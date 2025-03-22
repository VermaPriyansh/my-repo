import type { SimpleModel } from "./types"

/**
 * 用于创建 .env.example 文件，不要直接填写敏感信息。
 * 以 CLIENT_ 开头的变量会暴露给前端
 */
export const defaultEnv = {
  CLIENT_GLOBAL_SETTINGS: {
    APIKey: "",
    password: "",
    enterToSend: true
  },
  CLIENT_SESSION_SETTINGS: {
    title: "",
    saveSession: true,
    // 0-2
    APITemperature: 0.6,
    continuousDialogue: true,
    model: "gpt-4o-mini" as SimpleModel
  },
  CLIENT_DEFAULT_MESSAGE: ` PromptBridge AI
Empowering global users to write clearer, safer, and more effective AI prompts.

 Multilingual Input
Type your prompt in any of 50+ languages. PromptBridge will detect the language and translate it into optimized English for better AI performance.

 Prompt Validation
We check for grammar, ambiguity, and harmful language — and suggest ethical, inclusive alternatives when needed.

How to Use

Enter your prompt in the box above

Click “Validate Prompt”

View the corrected, safer version of your prompt

Copy and use it with your favorite AI tool!

Your data stays local — we don’t store or log anything.
`,
  CLIENT_MAX_INPUT_TOKENS: {
    "gpt-4o": 128 * 1000,
    "gpt-4o-mini": 128 * 1000
  } as Record<SimpleModel, number>,
  OPENAI_API_BASE_URL: "api.openai.com",
  OPENAI_API_KEY: "",
  TIMEOUT: 30000,
  PASSWORD: "",
  SEND_KEY: "",
  NO_GFW: false
}

export type SessionSettings = typeof defaultEnv.CLIENT_SESSION_SETTINGS
