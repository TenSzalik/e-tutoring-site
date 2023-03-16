const apiRequest = async (
  url: string = '',
  options: object | null = null,
  errMsg: string | null = null
) => {
  try {
    const response = await fetch(url, options)
    if (!response.ok) throw Error(response.status)
  } catch (err: object | any) {
    errMsg = err.message
  } finally {
    return errMsg
  }
}

export default apiRequest
