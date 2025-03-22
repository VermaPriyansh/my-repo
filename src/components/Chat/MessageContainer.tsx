import { type Accessor, For, Show, createEffect, createMemo } from "solid-js"
import { RootStore, defaultMessage } from "~/store"
import { scrollToBottom } from "~/utils"
import MessageItem from "./MessageItem"
import { defaultInputBoxHeight } from "./InputBox"
import { TransitionGroup } from "solid-transition-group"
import "~/styles/transition.css"

export default function ({
  sendMessage,
  inputBoxHeight
}: {
  sendMessage(value?: string): void
  inputBoxHeight: Accessor<number>
}) {
  const { store } = RootStore
  // 防止重新设置高度时页面跳动
  const paddingBottom = createMemo(
    k =>
      inputBoxHeight() === defaultInputBoxHeight - 1 ? k : inputBoxHeight(),
    defaultInputBoxHeight
  )

  createEffect((prev: number | undefined) => {
    if (prev !== undefined && store.messageList.length > prev) {
      scrollToBottom()
    }
    return store.messageList.length
  })

  createEffect(prev => {
    if (store.currentAssistantMessage) scrollToBottom()
  })

  createEffect(prev => {
    inputBoxHeight()
    if (prev && paddingBottom() !== defaultInputBoxHeight) {
      scrollToBottom()
    }
    return true
  })

  const shownTokens = (token: number) => {
    if (token > 1000) return (token / 1000).toFixed(1) + "k"
    else return token
  }

  return (
    <div
      class="px-1em"
      id="message-container"
      style={{
        "margin-bottom": `calc(6em + ${paddingBottom() + "px"})`
      }}
    >
      <div id="message-container-img" class="px-1em">
        <Show when={!store.messageList.length}>
          <MessageItem hiddenAction={true} message={defaultMessage} />
        </Show>
        <TransitionGroup name="transition-group">
          <For each={store.messageList}>
            {(message, index) => (
              <MessageItem
                message={message}
                hiddenAction={store.loading || message.type === "temporary"}
                index={index()}
                sendMessage={sendMessage}
              />
            )}
          </For>
        </TransitionGroup>
      </div>
      <Show
        when={!store.loading && (store.contextToken || store.inputContentToken)}
      >
        <div class="flex items-center px-1em text-0.8em">
          <hr class="flex-1 border-slate/40" />
          <hr class="flex-1  border-slate/30" />
        </div>
      </Show>
    </div>
  )
}
