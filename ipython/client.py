# function createPythonScriptProcess(targetFile, options) {
#   options = _.pick(options || {}, ['shell', 'cmd']);
#
#   const processOptions = getPythonCommandOptions(options),
#     cmd = options.cmd || 'python';
#
#   return processes.create(cmd, [targetFile], processOptions);
# }