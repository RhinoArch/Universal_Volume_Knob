from StudioOne import Application, Mixer, Plugin
app = Application()
mixer = app.getMixer()
track = mixer.getChannel("Your Track Name")
reverb_plugin = Plugin("Your Reverb Plugin Name")
reverb_plugin.insertToTrack(track)
reverb_plugin.setParameter("ParameterName", value)
app.saveDocument()
app.close()
