import * as Sentry from 'sentry-expo'

export const initSentry = () => {
  Sentry.init({
    dsn: '', //TODO: add your dsn
    enableInExpoDevelopment: true,
    debug: true, // If `true`, Sentry will try to print out useful debugging information if something goes wrong with sending the event. Set it to `false` in production
  })

  Sentry.Native.captureException('Sentry Exception')
}
